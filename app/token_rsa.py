import os, logging
from datetime import datetime, timedelta
from typing import Dict
import jwt
from Crypto.PublicKey import RSA

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_key = RSA.generate(int(os.getenv("TOKEN_RSA_BITS", 2048)))
_priv_pem = _key.export_key()
_pub_pem  = _key.publickey().export_key()

def issue_token(user_id: str, minutes: int = 30) -> str:
    payload = {"sub": user_id, "exp": datetime.utcnow() + timedelta(minutes=minutes)}
    token = jwt.encode(payload, _priv_pem, algorithm="RS256")
    logger.info("Token emitido para %s", user_id)
    return token

def verify_token(token: str) -> Dict:
    try:
        decoded = jwt.decode(token, _pub_pem, algorithms=["RS256"])
        logger.info("Token válido: %s", decoded["sub"])
        return decoded
    except Exception as e:
        logger.error("Token inválido: %s", e)
        raise
