from sqlalchemy.orm import Session
from app.schemas.user_schema import UserBase, UserRead, UserCreate
from app.db import dao
from app.errors.db_error import DBException
from app.utils.password_helper import PasswordGenerator, PasswordHash
from app.dependencies.config_dependency import get_settings
from app.utils.init_celery import celery


class UserService:
    @classmethod
    def create_user(cls, user: UserBase, db: Session) -> UserRead:
        response = PasswordGenerator().generate_password(get_settings().PASSWORD_LENGTH)

        print(f"*** Password -> {response.result}")

        hashed_password = PasswordHash.gen_hash_password(response.result)

        user_create = UserCreate(email=user.email, password=hashed_password)
        new_user = dao.create_user(user_create, db)

        if not new_user:
            raise DBException(f"Failed to create user with email {user.email}")

        return new_user

    @classmethod
    def send_email(cls, user: UserRead):
        subject = "Please verify your email"
        body = f"Thanks for registration.\n Your password is -> {user.password}"

        print("Sending Celery Tasks")
        celery.send_task(
            "email.send",
            (
                get_settings().MAIL_SENDER_NAME,
                get_settings().MAIL_SENDER_EMAIL,
                user.email,
                subject,
                body,
            ),
        )
