from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class DBException(HTTPException):
    message: str | None = None


def db_exception_handler(request: Request, exc: DBException):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": exc.message}
    )