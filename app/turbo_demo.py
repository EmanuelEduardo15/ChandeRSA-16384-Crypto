# app/turbo_demo.py

import sys
import os
import time
import json
import random
import hashlib
import logging
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Tuple, Dict

import gmpy2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Allow conversion of very large ints to str
sys.set_int_max_str_digits(10_000_000)
gmpy2.get_context().precision = 2048

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Paths for caching keys & validation reports
BASE_DIR      = Path(os.getenv("TURBO_BASE_DIR", "./"))
KEY_DIR       = BASE_DIR / "rsa_keys"
VALID_DIR     = BASE_DIR / "validation_reports"
KEY_DIR.mkdir(parents=True, exist_ok=True)
VALID_DIR.mkdir(parents=True, exist_ok=True)

# In-memory cache for fast reuse
rsa_key_cache: Dict[Tuple[int,int], Tuple[int,int,int,int,int,int,int,int,Dict,str]] = {}

MILLER_RABIN_ROUNDS = 64


def fast_prime(bits: int) -> int:
    """Generate a prime of given bit-length using gmpy2.next_prime."""
    rnd = gmpy2.mpz(random.getrandbits(bits) | (1 << (bits - 1)) | 1)
    return int(gmpy2.next_prime(rnd))


def modinv(a: int, m: int) -> int:
    """Compute modular inverse a⁻¹ mod m."""
    g, x, _ = gmpy2.gcdext(a, m)
    if g != 1:
        logger.error("No modular inverse for %d mod %d", a, m)
        raise ValueError("Modular inverse does not exist")
    return int(x % m)


def rsa_decrypt_crt(c: int, p: int, q: int, dp: int, dq: int, qinv: int) -> int:
    """CRT-optimized RSA decryption."""
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h  = (m1 - m2) * qinv % p
    return m2 + q * h


def validate_rsa_key(n: int, e: int, d: int, p: int, q: int) -> Dict:
    """Perform basic RSA key validation and return a report dict."""
    phi = (p - 1) * (q - 1)
    report = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "validation_steps": {
            "n_eq_pq":      (n == p * q),
            "e_coprime_phi": (gmpy2.gcd(e, phi) == 1),
            "e_d_inverse":  ((e * d) % phi == 1),
            "enc_dec_test": ((pow(pow(0xABCDEF1234567890, e, n), d, n) == 0xABCDEF1234567890)),
        },
    }
    # key size
    report["validation_steps"]["key_size"] = n.bit_length()
    # hash of public key
    pk_bytes = n.to_bytes((n.bit_length()+7)//8, "big") + e.to_bytes((e.bit_length()+7)//8, "big")
    report["validation_hash"] = hashlib.sha256(pk_bytes).hexdigest()
    report["is_valid"] = all(report["validation_steps"].values())
    logger.info("RSA-key validation: %s", report["is_valid"])
    return report


def get_rsa_keys_cached(bits: int, workers: int):
    """
    Generate or retrieve from cache an RSA keypair of 'bits' bits,
    along with CRT parameters and a validation report.
    """
    key = (bits, workers)
    if key in rsa_key_cache:
        return rsa_key_cache[key]

    half = bits // 2
    with ProcessPoolExecutor(max_workers=workers) as exe:
        p = exe.submit(fast_prime, half).result()
        q = exe.submit(fast_prime, half).result()

    n   = p * q
    phi = (p - 1) * (q - 1)
    e   = 65537
    d   = modinv(e, phi)
    dp  = d % (p - 1)
    dq  = d % (q - 1)
    qinv= modinv(q, p)

    # validate and write report
    report    = validate_rsa_key(n, e, d, p, q)
    report_id = report["validation_hash"][:16]
    report_path = VALID_DIR / f"validation_{report_id}.json"
    report_path.write_text(json.dumps(report, indent=2))

    rsa_key_cache[key] = (n, e, d, p, q, dp, dq, qinv, report, report_id)
    return rsa_key_cache[key]


def pipeline(message: str, bits: int = 16384, workers: int = 2) -> Tuple[str, float]:
    """
    Hybrid AES+RSA pipeline:
      - Retrieves or generates RSA keys
      - Encrypts 'message' with AES-256-CBC
      - Encrypts AES key with RSA
      - Decrypts AES key via CRT RSA
      - Decrypts message with AES
    Returns the plaintext and decryption time in seconds.
    """
    # load/generate keypair
    n, e, d, p, q, dp, dq, qinv, report, rid = get_rsa_keys_cached(bits, workers)

    # AES encryption
    aes_key = get_random_bytes(32)
    iv      = get_random_bytes(16)
    cipher  = AES.new(aes_key, AES.MODE_CBC, iv)
    ct      = cipher.encrypt(pad(message.encode(), AES.block_size))

    # RSA encrypt AES key
    key_int = int.from_bytes(aes_key, "big") % n
    enc_key = pow(key_int, e, n)

    # CRT decryption timing
    start = time.perf_counter()
    dec_int = rsa_decrypt_crt(enc_key, p, q, dp, dq, qinv)
    dec_time = time.perf_counter() - start

    # AES decryption
    aes_dec = dec_int.to_bytes(32, "big")
    pt = unpad(AES.new(aes_dec, AES.MODE_CBC, iv).decrypt(ct), AES.block_size).decode()

    # log to CSV
    csv_path = BASE_DIR / "rsa_turbo_log.csv"
    new_file = not csv_path.exists()
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow([
                "timestamp","bits","workers","pub_hash",
                "decrypt_s","msg_len","report_id"
            ])
        pub_hash = hashlib.sha256(n.to_bytes((n.bit_length()+7)//8,"big") + 
                                  e.to_bytes((e.bit_length()+7)//8,"big")).hexdigest()
        writer.writerow([
            datetime.utcnow().isoformat(), bits, workers, pub_hash,
            f"{dec_time:.3f}", len(message), rid
        ])

    return pt, dec_time
