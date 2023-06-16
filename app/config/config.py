from pydantic import BaseSettings
import os


base_dir = os.path.abspath(os.path.dirname(__name__))


class Settings(BaseSettings):
    SQLALCHEMY_URL: str | None #= 'sqlite///./insurance.db'

    class Config:
        env_file = os.path.join(base_dir, ".env.dev")

settings = Settings()