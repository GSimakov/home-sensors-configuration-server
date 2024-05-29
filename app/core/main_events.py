from typing import Callable
from fastapi import FastAPI
from loguru import logger

from app.utils.base_data.insert import insert

#todo fix api routes
def create_start_app_handler(
    app: FastAPI,
) -> Callable:
    async def start_app() -> None:
        await insert()
        # sudo docker container restart minio && sudo docker container restart magical_williams
        pass
    return start_app


def create_stop_app_handler(
        app: FastAPI
) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        pass
    return stop_app


