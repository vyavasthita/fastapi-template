from pydantic import BaseSettings
import os


base_dir = os.path.abspath(os.path.dirname(__name__))


class Settings(BaseSettings):
    SQLALCHEMY_URL: str | None
    JWT_ALGORITHM: str | None
    TOKEN_EXPIRY_TIME: int | None
    SECRET_KEY: str | None
    PASSWORD_LENGTH: int | None = 10

    class Config:
        env_file = os.path.join(base_dir, ".env.dev")

settings = Settings()