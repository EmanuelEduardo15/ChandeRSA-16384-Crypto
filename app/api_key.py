import os, logging
import binascii
from typing import Dict
from threading import Lock

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Simples armazenamento em memória; em prod use DB
_api_keys: Dict[str, str] = {}
_lock = Lock()

def generate_api_key(user_id: str) -> str:
    with _lock:
        if user_id in _api_keys:
            return _api_keys[user_id]
        key = binascii.hexlify(os.urandom(32)).decode()
        _api_keys[user_id] = key
        logger.info("API key gerada para %s", user_id)
        return key

def verify_api_key(user_id: str, api_key: str) -> bool:
    valid = _api_keys.get(user_id) == api_key
    logger.info("API key validação para %s: %s", user_id, valid)
    return valid
