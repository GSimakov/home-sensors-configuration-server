FROM python:3.11-alpine

WORKDIR /app

COPY ./pyproject.toml ./alembic.ini /app/

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip uninstall poetry -y


COPY . /app/


ENV ASYNC_DATABASE_URL="postgresql+asyncpg://admin:admin@localhost:5432/configs"
ENV DATABASE_URL="postgresql://admin:admin@localhost:5432/configs"


EXPOSE 8000

CMD alembic upgrade head && \
uvicorn app.main:app --port 8000 --host 0.0.0.0 --interface=asgi3

