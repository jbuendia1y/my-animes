import os
from jose import jwt

SECRET_KEY = os.environ.get("SECRET_KEY", "MY_SECRET_KEY")


def encode_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
