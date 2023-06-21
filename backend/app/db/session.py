from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.dependencies.config_dependency import get_settings


DATABASE_URL = None
engine = None

if get_settings().DB_TYPE == "SQLITE":
    DATABASE_URL = get_settings().SQLITE_URL

    engine = create_engine(url=DATABASE_URL, connect_args={"check_same_thread": False})

elif get_settings().DB_TYPE == "MYSQL":
    DATABASE_URL = (
        "mysql://"
        + get_settings().MYSQL_USER
        + ":"
        + get_settings().MYSQL_PASSWORD
        + "@"
        + get_settings().MYSQL_HOST
        + ":"
        + get_settings().MYSQL_PORT
        + "/"
        + get_settings().MYSQL_DB
    )

    engine = create_engine(url=DATABASE_URL)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
