from typing import Annotated
from fastapi import APIRouter, Depends
from app.dependencies.auth_dependency import UserAuthenticator
from app.schemas.auth_schema import Token
from app.service.auth_service import AuthService
from app.config.config import settings


auth_router = APIRouter(
    prefix="/api/auth"
)


@auth_router.post("/token", tags=["auth"], response_model=Token)
def token(
    user: Annotated[dict, Depends(UserAuthenticator())]
) -> Token:
    access_token = AuthService.create_access_token(user.get('email'), settings.TOKEN_EXPIRY_TIME)

    return {"access_token": access_token, "token_type": "bearer"}
