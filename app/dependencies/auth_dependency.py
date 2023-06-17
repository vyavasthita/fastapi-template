from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.db_dependency import get_db
from app.service.auth_service import AuthService
from app.errors.auth_error import AuthException


class UserAuthenticator:
    def __call__(
            self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
            db: Annotated[Session, Depends(get_db)]
        ):
        user = AuthService.verify_user(email=form_data.username, db=db)

        if not AuthService.verify_password(user, form_data.password):
            raise AuthException("Invalid Password")
       
        return {
            'email': form_data.username, 
            'password': form_data.password
        }