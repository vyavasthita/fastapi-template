from typing import Annotated
from pydantic import BaseModel, validator, root_validator
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status, Body
from app.errors.user_error import UserValidationException
from app.dependencies.config_dependency import get_settings


class UserBase(BaseModel):
    email: str = Body(title="Email Address")

    @validator("email")
    def validate_email(cls, email_address):
        try:
            email_info = validate_email(email_address, check_deliverability=True)
        except EmailNotValidError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

        return email_address
    
class UserName(UserBase):
    first_name: Annotated[
        str,
        Body(
            title="First Name",
            description="First Name of the user",
            min_length=2,
            max_length=30,
        ),
    ]
    last_name: Annotated[
        str,
        Body(
            title="Last Name",
            description="Last Name of the user",
            min_length=2,
            max_length=30,
        ),
    ]


class UserCreate(UserName):
    password: Annotated[
        str,
        Body(
            title="Password",
            description="Password of the user",
            min_length=get_settings().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]
    confirm_password: Annotated[
        str,
        Body(
            title="Confirm Password",
            description="Confirm New Password",
            min_length=get_settings().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]

    @root_validator()
    def verify_password_match(cls, values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise UserValidationException("The passwords did not match.")

        return values

class UserProfileUpdate(BaseModel):
    age: Annotated[int, Body(title="Age", description="Age of the user", ge=1)] = 1


class UserPasswordUpdate(BaseModel):
    existing_password: Annotated[
        str, Body(title="Existing Password", description="Existing Password")
    ]
    new_password: Annotated[
        str,
        Body(
            title="New Password",
            description="New Password to be updated",
            min_length=get_settings().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]
    confirm_password: Annotated[
        str,
        Body(
            title="Confirm New Password",
            description="Confirm New Password",
            min_length=get_settings().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]

    @root_validator()
    def verify_password_match(cls, values):
        password = values.get("new_password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise UserValidationException("The two passwords did not match.")

        return values


class UserRead(UserName):
    id: int

    class Config:
        orm_mode = True


class UserProfileUpdateRead(UserBase, UserProfileUpdate):
    id: int

    class Config:
        orm_mode = True
