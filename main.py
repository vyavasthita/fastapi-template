from fastapi import FastAPI
from app.routers.user_router import user_router
from app.errors.db_error import DBException, db_exception_handler


app = FastAPI()


from app.db import init


app.add_exception_handler(DBException, db_exception_handler)
app.include_router(user_router)