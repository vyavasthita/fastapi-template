from typing import Annotated
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from app.dependencies.db_dependency import get_db
from app.schemas.user_schema import UserRead, UserCreate
from app.db.dao import create_user
from app.errors.db_error import DBException


user_router = APIRouter(
    prefix="/api"
)


@user_router.post("/users", tags=["register"], response_model=UserRead)
def create(
    user: Annotated[UserCreate, Body()],
    db: Session = Depends(get_db)
) -> UserRead:
    new_user = create_user(user, db)

    if not new_user:
        raise DBException(f"Failed to create user with email {user.email}")
    
    return new_user
    
