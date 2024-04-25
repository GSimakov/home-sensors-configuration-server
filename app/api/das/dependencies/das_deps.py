from uuid import UUID
from fastapi import Path
from typing_extensions import Annotated

from app import crud
from app import models

__all__ = ['get_das_by_board_hardware_id_from_path']

model = models.DataAcquisitionSystem
crud_board = crud.board
crud_das = crud.das


async def get_das_by_board_hardware_id_from_path(
        hardware_id: Annotated[str, Path(description='Hardware id of board')]
) -> model:
    current_board = await crud_board.get_by_hardware_id(hardware_id=hardware_id)
    return current_board.das
