from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.dependencies.config_dependency import get_settings


engine = create_engine(
    url=get_settings().SQLALCHEMY_URL, 
    connect_args={
        "check_same_thread": False
    }
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
