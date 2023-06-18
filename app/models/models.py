from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(60), index=True, unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)

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

    userprofile_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    user = relationship("User", back_populates="profile")

    def __init__(self, first_name: str, last_name: str, age: int, user: User) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.userprofile = user

    def __repr__(self) -> str:
        return f"User({self.first_name} {self.last_name})"
