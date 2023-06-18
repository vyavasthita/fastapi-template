from jose import jwt, JWTError
from app.errors.auth_error import AuthException
from app.logging.api_logger import ApiLogger


def create_access_token(data: dict, secret_key: str, algorithm: str) -> str:
    ApiLogger.log_debug(f"Creating access token with data {data}.")

    try:
        return jwt.encode(data, secret_key, algorithm)
    except JWTError as error:
        ApiLogger.log_error(f"Failed to create access token. {str(error)}.")

        raise AuthException("Failed to create access token")


def decode_access_token(token: str, secret_key: str, algorithm: str) -> str:
    try:
        return jwt.decode(token, secret_key, algorithms=algorithm)
    except JWTError as error:
        ApiLogger.log_error(f"Failed to decode access token. {str(error)}.")
        raise AuthException("Token expired or invalid.")
