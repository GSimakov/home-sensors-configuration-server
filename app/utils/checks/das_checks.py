from uuid import UUID

from app import models
from app import crud
from app.utils.exceptions import NameExistException, IdNotFoundException

__all__ = ['das_hardware_id_is_taken']

crud_repo = crud.das
model = models.DAS


async def das_hardware_id_is_taken(hardware_id: str) -> None:
    obj = await crud_repo.get_by_hardware_id(hardware_id=hardware_id)
    if obj:
        raise