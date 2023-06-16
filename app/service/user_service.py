from sqlalchemy.orm import Session
from app.schemas.user_schema import UserBase, UserRead, UserCreate
from app.db.dao import create_user
from app.errors.db_error import DBException
from app.utils.password_helper import PasswordGenerator, PasswordHash
from app.config.config import settings


class UserService:
    password_generator: PasswordGenerator = PasswordGenerator(settings.PASSWORD_LENGTH)
    password_hash: PasswordHash = PasswordHash()    

    @classmethod
    def create_user(cls, user: UserBase, db: Session) -> UserRead:
        response = cls.password_generator.generate_password()
        
        hashed_password = cls.password_hash.gen_hash_password(response.result)

        user_create = UserCreate(email=user.email, password=hashed_password)
        new_user = create_user(user_create, db)

        if not new_user:
            raise DBException(f"Failed to create user with email {user.email}")
        
        return new_user