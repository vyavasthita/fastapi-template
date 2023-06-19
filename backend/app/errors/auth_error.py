from fastapi import Request, status
from fastapi.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class AuthException(Exception):
    message: str | None = None


def auth_exception_handler(request: Request, exc: AuthException):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": exc.message},
    )
