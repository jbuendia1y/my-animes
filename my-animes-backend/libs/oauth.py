from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from libs.token import decode_token
from libs import errors

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise errors.INVALID_AUTH_CREDENTIALS
    return payload
