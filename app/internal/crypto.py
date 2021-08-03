import hashlib
import hmac
from typing import Optional
import base64


# for example. use ENV in future
SECRET_KEY = "98288a54b00ffaaefe4d66bd71becb050d4db3aadb2590e7b8fbe3f74656604"
PASSWORD_SALT = "a6e975ceb69c40e1895c7bda2e34d419eae2ed286eb0eca1a6c1509d932be157"


def sign_data(data: str) -> str:
    """ Sign data """
    return hmac.new(
        SECRET_KEY.encode(),
        msg=data.encode(),
        digestmod=hashlib.sha256
    ).hexdigest().upper()


def get_username_from_signed_data(data: str) -> Optional[str]:
    try:
        username_base64, sign = data.split('.')
        username = base64.b64decode(username_base64.encode()).decode()
        valid_sign = sign_data(username)
    except Exception:
        return None

    if hmac.compare_digest(sign, valid_sign):
        return username
    return None


def verify_password(password: str, password_hash: str) -> bool:
    return hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest().lower() == password_hash.lower()