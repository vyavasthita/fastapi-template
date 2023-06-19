from typing import List, Union
from pydantic import BaseSettings, validator, AnyHttpUrl
import os


base_dir: str = os.path.abspath(os.path.dirname(__name__))


class DevSettings(BaseSettings):
    DB_TYPE: str | None = "SQLITE"
    SQLITE_URL: str | None
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
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]

    MYSQL_USER: str
    MYSQL_HOST: str
    MYSQL_DB: str
    MYSQL_PORT: str

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        env_file = os.path.join(base_dir, ".env.dev")


class AutTestSettings(BaseSettings):
    DB_TYPE: str | None = "SQLITE"
    SQLITE_URL: str | None
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
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]

    MYSQL_USER: str
    MYSQL_HOST: str
    MYSQL_DB: str
    MYSQL_PORT: str

    @validator("BACKEND_CORS_ORIGINS", pre=True)  # 3
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v

        raise ValueError(v)

    class Config:
        env_file = os.path.join(base_dir, ".env.aut_test")
