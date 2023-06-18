#!/bin/bash

# NAME=fastapi-template
# WORKERS=1
# WORKER_CLASS=uvicorn.workers.UvicornWorker
# LOG_LEVEL=error

# poetry run gunicorn main:app \
#   --name $NAME \
#   --workers $WORKERS \
#   --worker-class $WORKER_CLASS \
#   --log-level=$LOG_LEVEL \
#   --log-file=-

poetry run gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
