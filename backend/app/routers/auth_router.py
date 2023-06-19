from typing import Annotated
from fastapi import APIRouter, Depends
from app.dependencies.auth_dependency import UserAuthenticator
from app.schemas.auth_schema import Token
from app.service.auth_service import AuthService
from app.dependencies.config_dependency import get_settings


auth_router = APIRouter(prefix="/api/auth")


@auth_router.post("/token", tags=["Auth"], response_model=Token)
def token(user: Annotated[dict, Depends(UserAuthenticator())]) -> Token:
    access_token = AuthService.create_access_token(
        user.get("email"), get_settings().TOKEN_EXPIRY_TIME
    )

    return {"access_token": access_token, "token_type": "bearer"}
