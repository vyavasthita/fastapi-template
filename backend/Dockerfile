FROM python:3.10.12-alpine3.18 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml /tmp
COPY poetry.lock* /tmp

RUN poetry export -f requirements.txt --only core --only dev --only aut-test --output requirements.txt --without-hashes

FROM python:3.10.12-alpine3.18

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

WORKDIR /app

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Expose the port 5001 in which our application runs
EXPOSE 5001

ARG DB_TYPE=MYSQL
ENV DB_TYPE=${DB_TYPE}

# Copy requirements from host, to docker container in /app 
# COPY ./requirements.txt .
# Install the dependencies
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install mysqlclient

# Copy everything from ./worker directory to /app in the container
COPY app /app/app
COPY alembic /app/alembic
COPY alembic.ini .
COPY main.py .
# Copy files for unit tests
COPY tests /app/tests
COPY .coveragerc .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]
