from pydantic import validator
from pydantic_settings import BaseSettings

import logging
import sys
from typing import Any, Tuple

from loguru import logger
from pydantic import PostgresDsn

from app.core.logging import InterceptHandler


class AppSettings(BaseSettings):
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str = "Valeria"
    ASYNC_DATABASE_URL: PostgresDsn | str
    DATABASE_URL: PostgresDsn | str
    DB_POOL_SIZE: int = 1
    MAX_OVERFLOW: int = 1

    SECRET_KEY: str

    allowed_hosts: list[str] = ["*"]

    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Valeria"
    version: str = "0.0.0"

    api_prefix: str = "/Valeria"

    jwt_token_prefix: str = "Token"

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")


    @validator("ASYNC_DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=str(values.get("DATABASE_PORT")),
            path=f"/{values.get('DATABASE_NAME') or ''}",
        )

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])

    class Config:
        case_sensitive = True
        env_file = '.env'

#todo переделать енвешку
