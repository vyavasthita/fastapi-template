# Prerequisites

sudo apt update && sudo apt upgrade
sudo apt-get install rabbitmq-server

sudo apt install redis-server


fastapi
uvicorn
python-dotenv
email-validator
passlib[bcrypt]
python-jose
python-multipart
sqlalchemy
celery
redis
gunicorn

# Running with Gunicorn
poetry run gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
