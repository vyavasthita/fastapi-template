from fastapi import Request, status
from fastapi.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class UserValidationException(Exception):
    message: str | None = None


def user_validation_exception_handler(request: Request, exc: UserValidationException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": exc.message},
    )
