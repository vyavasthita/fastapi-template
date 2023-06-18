from typing import Annotated
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from app.dependencies.db_dependency import get_db
from app.schemas.user_schema import UserBase, UserRead
from app.service.user_service import UserService


user_router = APIRouter(
    prefix="/api"
)


@user_router.post("/users", tags=["register"], response_model=UserRead)
def create(
    user: Annotated[UserBase, Body()],
    db: Session = Depends(get_db)
) -> UserRead:
    user = UserService.create_user(user, db)
    UserService.send_email(user)
    return user

    
