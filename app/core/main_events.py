from typing import Callable
from fastapi import FastAPI
from loguru import logger

from app.crud import user

def create_start_app_handler(
    app: FastAPI,
) -> Callable:
    async def start_app() -> None:
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)
        lalala = await user.get_count_wrapped()
        print(lalala)

        # sudo docker container restart minio && sudo docker container restart magical_williams
    return start_app


def create_stop_app_handler(
        app: FastAPI
) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        pass
    return stop_app


