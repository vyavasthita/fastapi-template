from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from app.db import dao
from app.errors.auth_error import AuthException
from app.models.models import User
from app.utils.security import create_access_token
from app.dependencies.config_dependency import get_settings
from app.utils.password_helper import PasswordHash


class AuthService:
    @classmethod
    def create_access_token(cls, email: str, expires_delta: timedelta | None = None):
        expiry_time = None

        if expires_delta:
            expiry_time = datetime.utcnow() + timedelta(minutes=expires_delta)
        else:
            expiry_time = datetime.utcnow() + timedelta(minutes=15)

        return create_access_token(
            dict(sub=email, exp=expiry_time), 
            get_settings().SECRET_KEY, 
            algorithm=get_settings().JWT_ALGORITHM
        )

    @classmethod
    def validate_token(cls, data: dict, db: Session) -> User:
        email = data.get('sub')

        if not email:
            raise AuthException("Invalid Token")
        
        return cls.verify_user(email=email, db=db)
    
    @classmethod
    def verify_user(cls, email: str, db: Session) -> User:        
        user = dao.get_user_by_email(email=email, db=db)

        if not user:
            raise AuthException("User not found")
        
        return user
    
    @classmethod
    def verify_password(cls, user: User, password: str) -> bool:
        return PasswordHash.verify_password(password, user.password)