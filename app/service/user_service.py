from typing import Annotated
from sqlalchemy.orm import Session
from app.schemas.user_schema import (
    UserBase,
    UserRead,
    UserCreate,
    UserProfileUpdate,
    UserProfileUpdateRead,
)
from app.db import dao
from app.errors.db_error import DBException
from app.utils.password_helper import PasswordGenerator, PasswordHash
from app.utils.init_celery import celery
from app.dependencies.config_dependency import get_settings
from app.models.models import User
from app.logging.api_logger import ApiLogger


class UserService:
    @classmethod
    def create_user(cls, user: UserBase, db: Session) -> UserRead:
        response = PasswordGenerator().generate_password(get_settings().PASSWORD_LENGTH)

        ApiLogger.get_instance().log_info(f"*** Password -> {response.result}")

        hashed_password = PasswordHash.gen_hash_password(response.result)

        user_create = UserCreate(email=user.email, password=hashed_password)
        new_user = dao.create_user(user_create, db)

        if not new_user:
            raise DBException(f"Failed to create user with email {user.email}")

        cls.send_user_registration_email(user=new_user)

        return new_user

    @classmethod
    def update_profile_info(
        cls,
        current_user: User,
        user_info: UserProfileUpdate,
        db: Session,
    ) -> UserProfileUpdateRead:
        user = dao.update_user_profile(current_user, user_info, db)

        if not user:
            raise DBException(f"Failed to update user profile for {current_user.email}")

        return user

    @classmethod
    def update_password(
        cls,
        current_user: User,
        password: str,
        db: Session,
    ) -> None:
        hashed_password = PasswordHash.gen_hash_password(password)
        dao.update_user_password(current_user, hashed_password, db)

    @classmethod
    def reset_password(
        cls,
        user: User,
        db: Session,
    ) -> None:
        response = PasswordGenerator().generate_password(get_settings().PASSWORD_LENGTH)

        ApiLogger.get_instance().log_info(f"*** Password -> {response.result}")

        hashed_password = PasswordHash.gen_hash_password(response.result)

        dao.update_user_password(user, hashed_password, db)

        cls.send_reset_password_email(user=user)

    @classmethod
    def send_user_registration_email(cls, user: User):
        subject = "Please verify your email"
        body = f"Thanks for registration.\nYour password is -> {user.password}"

        ApiLogger.get_instance().log_info(
            f"Sending Verfication Email to '{user.email}'"
        )

        celery.send_task(
            "email.send",
            (
                get_settings().MAIL_SENDER_NAME,
                get_settings().MAIL_SENDER_EMAIL,
                "User",
                user.email,
                subject,
                body,
            ),
        )

    @classmethod
    def send_reset_password_email(cls, user: User):
        subject = "Password Reset"
        body = f"As per your request.\nYour new password is -> {user.password}"

        print("Sending Password Reset Email")
        celery.send_task(
            "email.send",
            (
                get_settings().MAIL_SENDER_NAME,
                get_settings().MAIL_SENDER_EMAIL,
                "User",
                user.email,
                subject,
                body,
            ),
        )
