from celery import Celery
from app.config.config import settings


celery = Celery(__name__, broker=settings.CELERY_BROKER_URL, 
                result_backend=settings.CELERY_RESULT_BACKEND)
