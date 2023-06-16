from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.db_dependency import get_db
from app.schemas.auth_schema import Token
from app.service.auth_service import AuthService
from app.errors.auth_error import AuthException
from app.config.config import settings


auth_router = APIRouter(
    prefix="/api/auth"
)


class UserAuthenticator:
    def __call__(
            self, form_data: OAuth2PasswordRequestForm = Depends(), 
            db = Depends(get_db)
        ):
        user = AuthService.verify_user(email=form_data.username, db=db)

        if not AuthService.verify_password(user, form_data.password):
            raise AuthException("Invalid Password")
       
        return {
            'email': form_data.username, 
            'password': form_data.password
        }

@auth_router.post("/token", tags=["auth"], response_model=Token)
def token(
    user: Annotated[dict, Depends(UserAuthenticator())],
    db: Session = Depends(get_db)
) -> Token:
    access_token = AuthService.create_access_token(user.get('email'), settings.TOKEN_EXPIRY_TIME)

    return {"access_token": access_token, "token_type": "bearer"}
    

    
