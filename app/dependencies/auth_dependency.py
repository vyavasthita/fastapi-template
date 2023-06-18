from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.db_dependency import get_db
from app.service.auth_service import AuthService
from app.errors.auth_error import AuthException
from app.logging.api_logger import ApiLogger


def get_auth_schema():
    return OAuth2PasswordBearer(tokenUrl="/api/auth/login")


class UserAuthenticator:
    def __call__(
        self,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info(f"Verifying user with email '{form_data.username}'.")
        user = AuthService.verify_user(email=form_data.username, db=db)

        ApiLogger.log_info(f"Verifying user has provided correct password.")
        if not AuthService.verify_password(user, form_data.password):
            raise AuthException("Invalid Password")

        return {"email": form_data.username, "password": form_data.password}
