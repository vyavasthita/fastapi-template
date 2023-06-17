from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.errors.auth_error import AuthException


oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/auth/login')


def create_access_token(data: dict, secret_key: str, algorithm: str) -> str:
    try:
        return jwt.encode(data, secret_key, algorithm)
    except JWTError as error:
        raise AuthException("Failed to create access token")
    
def decode_access_token(token: str, secret_key: str, algorithm: str) -> str:
    try:
        return jwt.decode(token, secret_key, algorithms=algorithm)
    except JWTError as error:
        raise AuthException("Failed to create access token")