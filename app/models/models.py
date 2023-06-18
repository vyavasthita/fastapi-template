from app.db.base import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(60), index=True, unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    is_admin = Column(Boolean, default=False)

    profile = relationship("Profile", back_populates="user", uselist=False)

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        is_admin: bool = False,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"User({self.first_name} {self.last_name})"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    is_activated = Column(Boolean, default=False)

    userprofile_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    user = relationship("User", back_populates="profile")

    def __init__(self, age: int, user: User, is_activated: bool = False) -> None:
        self.age = age
        self.userprofile = user
        self.is_activated = is_activated

    def __repr__(self) -> str:
        return f"User({self.age})"
