from app.db.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(60), index=True, unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User({self.email})"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    age = Column(Integer)
