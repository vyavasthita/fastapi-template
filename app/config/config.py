from pydantic import BaseSettings
import os


base_dir: str = os.path.abspath(os.path.dirname(__name__))


class DevSettings(BaseSettings):
    SQLALCHEMY_URL: str | None
    JWT_ALGORITHM: str | None
    TOKEN_EXPIRY_TIME: int | None
    SECRET_KEY: str | None
    PASSWORD_LENGTH: int | None = 10
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    MAIL_SENDER_NAME: str
    MAIL_SENDER_EMAIL: str
    # Configuration file for logging
    LOG_CONFIG_FILE: str
    # Directory where logs will be generated.
    LOGS_DIR: str
    # Log File name
    LOG_FILE_NAME: str

    class Config:
        env_file = os.path.join(base_dir, ".env.dev")


class AutTestSettings(BaseSettings):
    SQLALCHEMY_URL: str | None
    JWT_ALGORITHM: str | None
    TOKEN_EXPIRY_TIME: int | None
    SECRET_KEY: str | None
    PASSWORD_LENGTH: int | None = 10
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    MAIL_SENDER_NAME: str
    MAIL_SENDER_EMAIL: str
    # Configuration file for logging
    LOG_CONFIG_FILE: str
    # Directory where logs will be generated.
    LOGS_DIR: str
    # Log File name
    LOG_FILE_NAME: str

    class Config:
        env_file = os.path.join(base_dir, ".env.aut_test")
