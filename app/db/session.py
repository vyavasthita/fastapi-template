from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import settings


engine = create_engine(url=settings.SQLALCHEMY_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
