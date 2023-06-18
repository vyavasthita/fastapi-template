import os
from fastapi import FastAPI
from app.routers.auth_router import auth_router
from app.routers.user_router import user_router
from app.errors.db_error import DBException, db_exception_handler
from app.errors.auth_error import AuthException, auth_exception_handler
from app.dependencies.config_dependency import get_settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


from app.db import init


app.add_exception_handler(DBException, db_exception_handler)
app.add_exception_handler(AuthException, auth_exception_handler)

app.include_router(user_router)
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=get_settings().ALLOW_METHODS,
    allow_headers=get_settings().ALLOW_HEADERS,
)


def create_log_directory():
    base_dir = os.path.abspath(os.path.dirname(__name__))

    if not os.path.exists(os.path.join(base_dir, get_settings().LOGS_DIR)):
        os.mkdir(os.path.join(base_dir, get_settings().LOGS_DIR))


create_log_directory()
