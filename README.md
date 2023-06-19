# indian-insurance
FastAPI template

# Python Version
3.10.6

# Testing Platform

1. OS - Ubuntu 22.04
2. Docker Compose version v2.17.3
3. Docker version 23.0.6

# Prerequisites

sudo apt update && sudo apt upgrade
sudo apt-get install rabbitmq-server

sudo apt install redis-server

# Python Packages Used
- fastapi
- uvicorn
- python-dotenv
- email-validator
- passlib[bcrypt]
- python-jose
- python-multipart
- sqlalchemy
- celery
- redis
- gunicorn
- alembic

Dev Env;-
- black

# Webserver
gunicorn + uvicorn

# Sending email
Ref: TBD

# Celery Worker
TBD

# To remove all pyc and __pycache__ files
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

# Alembic
poetry run alembic revision -m "First migration"

poetry run alembic upgrade head

# Source Code Folder Structure

```bash
|-- README.md
|-- alembic
|   |-- README
|   |-- env.py
|   |-- script.py.mako
|   `-- versions
|       |-- 3c2d9f412fc7_first_migration.py
|       `-- b2c65ce21236_update_profile.py
|-- alembic.ini
|-- app
|   |-- config
|   |   |-- config.py
|   |   `-- logging.conf
|   |-- db
|   |   |-- base.py
|   |   |-- dao.py
|   |   |-- init.py
|   |   `-- session.py
|   |-- dependencies
|   |   |-- auth_dependency.py
|   |   |-- config_dependency.py
|   |   `-- db_dependency.py
|   |-- errors
|   |   |-- auth_error.py
|   |   `-- db_error.py
|   |-- logging
|   |   `-- api_logger.py
|   |-- models
|   |   `-- models.py
|   |-- routers
|   |   |-- auth_router.py
|   |   `-- user_router.py
|   |-- schemas
|   |   |-- auth_schema.py
|   |   `-- user_schema.py
|   |-- service
|   |   |-- auth_service.py
|   |   `-- user_service.py
|   `-- utils
|       |-- init_celery.py
|       |-- password_helper.py
|       |-- response.py
|       `-- security.py
|-- app.db
|-- gunicorn_start.sh
|-- main.py
|-- poetry.lock
`-- pyproject.toml
```

# Assumptions
TBD

# DB Schema
1. User
    id, integer, PK
    email, string(60), indexed, unique, not null
    password, string(200), not null

2. Profile
    id, integer, PK
    first_name, string(30), not null
    last_name, string(30), not null
    age, integer, not null
    
    FK - User.id

# Best Practices followed
01. Production web server gunicorn
02. Normalized DB Schema
03. Python Logging - Console and File
04. Hashing of generated password
05. Use of exception handling
06. Proper HTTP status codes
07. API documentation using swagger
08. Type annotations are added for all methods.
09. Different configurations for differnent environments like Dev, test, QA, Production.
10. Use of environment variables.
11. Proper directory and file structure of source code.
12. Detailed README file.
13. Proper git commit messages. Every commit is done post completing a functionality.
14. Pep8 naming convention for modules, classes, methods, functions and variables.
15. Comments added wherever required.
16. Poetry used for python package configuration
17. Sending Email is done by using background tasks using Celery, RabbitMQ, Redis.
18. Manual steps are minimal while testing the app.
19. Code formatting is done using black
20. Import statements are in order.
    - Python core -> flask -> flask third party -> application modules

    Also related modules are imported in order.

# TBD
    Doc string added for all modules and methods
    Docker with docker compose used. Both Sqlite and production db mysql is used.
    Unit tests with coverage report
    Use of sqlalchemy transaction for rollback if failure.
    Use of Makefile for ease of use.

# Validations Done
01. Duplicated email during registration are validated.
02. Invalid credentials while sign in
03. Extra attribute is passed in request.
04. Required attribute is not passed in request.
05. Email address is in invalid format or invalid domain used.
06. Customer Name attribute's is greator than 50 characters.

# Testing
- This app is tested on Ubuntu 22.04 LTS.

# HTTP Status code used
- HTTP_200_OK = 200
- HTTP_201_CREATED = 201
- HTTP_400_BAD_REQUEST = 400
- HTTP_404_NOT_FOUND = 404
- HTTP_422_UNPROCESSABLE_ENTITY = 422
- HTTP_500_INTERNAL_SERVER_ERROR = 500

## How to Test

1. Clone the repo
2. Go to root directory 'fastapi-template'.
