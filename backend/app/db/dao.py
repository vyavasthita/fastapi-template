from sqlalchemy.orm import Session
from app.schemas.user_schema import (
    UserCreate,
    UserProfileUpdate,
    UserProfileUpdateRead,
)
from app.models.models import User, Profile


def create_user(user: UserCreate, db: Session) -> User:
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user_by_id(user: User, db: Session) -> User:
    db.query(User).filter_by(id=user.id).delete()
    db.commit()


def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter_by(email=email).first()


def get_user_by_id(user_id: int, db: Session) -> User:
    return db.query(User).get(user_id)


def update_user_profile(
    user: User, user_info: UserProfileUpdate, db: Session
) -> UserProfileUpdateRead:
    user.first_name = user_info.first_name
    user.last_name = user_info.last_name

    profile = db.query(Profile).filter(Profile.userprofile_id == user.id).first()

    if profile:  # record already exists
        # Update the record
        profile.age = user_info.age
    else:  # new record
        profile = Profile(age=user_info.age, user=user.id)

    db.add(profile)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.refresh(profile)

    return user


def update_user_password(user: User, password: str, db: Session) -> None:
    user.password = password

    db.add(user)
    db.commit()
    db.refresh(user)
