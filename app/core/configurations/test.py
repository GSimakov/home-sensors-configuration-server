import logging

from app.core.configurations.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test Valeria"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = "test.env"

