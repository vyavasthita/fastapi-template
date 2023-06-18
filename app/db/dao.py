from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models.models import User


def create_user(user: UserCreate, db: Session) -> User:
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter_by(email=email).first()
