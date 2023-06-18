from pydantic import BaseModel, validator
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status


class UserBase(BaseModel):
    email: str

    @validator("email")
    def validate_email(cls, email_address):
        try:
            email_info = validate_email(email_address, check_deliverability=True)
        except EmailNotValidError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

        return email_address


class UserCreate(UserBase):
    password: str


class UserRead(UserCreate):
    id: int

    class Config:
        orm_mode = True
