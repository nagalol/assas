import time
from typing import Dict
import jwt
from decouple import config

def token_response(token: str):
    return {
        "access_token": token
    }

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 2400
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM).decode()

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token.encode(), JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}