from celery import Celery
from app.dependencies.config_dependency import get_settings


celery = Celery(
    __name__,
    broker=get_settings().CELERY_BROKER_URL,
    result_backend=get_settings().CELERY_RESULT_BACKEND,
)
