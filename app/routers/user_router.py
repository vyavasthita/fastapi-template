from typing import Annotated
from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.orm import Session
from app.dependencies.db_dependency import get_db
from app.dependencies.auth_dependency import (
    get_auth_schema,
    ValidateToken,
    ValidateDuplicateUser,
    ValidatePassword,
)
from app.schemas.user_schema import (
    UserBase,
    UserRead,
    UserProfileUpdate,
    UserProfileUpdateRead,
    UserProfilePasswordUpdate,
)
from app.service.user_service import UserService
from app.service.auth_service import AuthService
from app.models.models import User


user_router = APIRouter(prefix="/api")


@user_router.post("/users", tags=["register"], response_model=UserRead)
def create(
    user: Annotated[dict, Depends(ValidateDuplicateUser())],
    db: Session = Depends(get_db),
) -> UserRead:
    user = UserService.create_user(user, db)
    UserService.send_email(user)
    return user


@user_router.put(
    "/users/profile", tags=["profile"], response_model=UserProfileUpdateRead
)
def update(
    current_user: Annotated[dict, Depends(ValidateToken())],
    user_info: Annotated[UserProfileUpdate, Body()],
    db: Session = Depends(get_db),
) -> UserProfileUpdateRead:
    return UserService.update_profile_info(current_user, user_info, db)


@user_router.put(
    "/users/profile/password", tags=["profile"], status_code=status.HTTP_204_NO_CONTENT
)
def update(
    user_info: Annotated[dict, Depends(ValidatePassword())],
    db: Session = Depends(get_db),
) -> None:
    return UserService.update_password(user_info.get('user'), user_info.get('password'), db)


@user_router.get("/users/me", tags=["profile"], response_model=UserRead)
def me(
    token: Annotated[str, Depends(get_auth_schema())], db: Session = Depends(get_db)
) -> UserRead:
    return AuthService.get_current_user(token, db)
