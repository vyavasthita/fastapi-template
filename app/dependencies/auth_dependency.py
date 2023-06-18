from typing import Annotated
from fastapi import Depends, Body
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.db_dependency import get_db
from app.service.auth_service import AuthService
from app.errors.auth_error import AuthException
from app.logging.api_logger import ApiLogger
from app.schemas.user_schema import UserBase, UserCreate, UserPasswordUpdate


def get_auth_schema():
    return OAuth2PasswordBearer(tokenUrl="/api/auth/token")


class ValidateDuplicateUser:
    def __call__(
        self,
        user: Annotated[UserCreate, Body()],
        db: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info(f"Verifying user with email '{user.email}'.")
        existing_user = AuthService.check_user(email=user.email, db=db)

        if existing_user:
            raise AuthException(
                f"Duplicate Email. User already exists with email '{user.email}'."
            )

        return user


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


class ValidateToken:
    def __call__(
        self,
        token: Annotated[str, Depends(get_auth_schema())],
        db: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info("Verifying token.")
        return AuthService.get_current_user(token=token, db=db)


class ValidatePassword:
    def __call__(
        self,
        token: Annotated[str, Depends(get_auth_schema())],
        user_info: Annotated[UserPasswordUpdate, Body()],
        db: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info("Verifying token.")
        user = AuthService.get_current_user(token=token, db=db)

        if not AuthService.verify_password(user, user_info.existing_password):
            raise AuthException("Invalid Existing Password")

        return {"user": user, "password": user_info.new_password}


class ValidatePasswordReset:
    def __call__(
        self,
        user: Annotated[UserBase, Body()],
        db: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info(f"Verifying user with email '{user.email}'.")
        return AuthService.verify_user(email=user.email, db=db)


class ValidateDeleteAccount:
    def __call__(
        self,
        token: Annotated[str, Depends(get_auth_schema())],
        db: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info("Verifying token.")
        return AuthService.get_current_user(token=token, db=db)
