from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserProfileUpdate, UserProfileUpdateRead
from app.models.models import User, Profile


def create_user(user: UserCreate, db: Session) -> User:
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user_by_id(user: User, db: Session) -> User:
    db.query(User).filter_by(id=user.id).delete()
    db.commit()


def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter_by(email=email).first()


def update_user_profile(
    user: User, user_info: UserProfileUpdate, db: Session
) -> UserProfileUpdateRead:
    profile = db.query(Profile).filter(Profile.userprofile_id == user.id).first()

    if profile:  # record already exists
        # Update the record
        profile.first_name = user_info.first_name
        profile.last_name = user_info.last_name
        profile.age = user_info.age
    else:  # new record
        profile = Profile(
            first_name=user_info.first_name,
            last_name=user_info.last_name,
            age=user_info.age,
            user=user.id,
        )

    db.add(profile)
    db.commit()
    db.refresh(profile)
    return user


def update_user_password(
    user: User, password: str, db: Session
) -> UserProfileUpdateRead:
    user.password = password

    db.add(user)
    db.commit()
    db.refresh(user)
