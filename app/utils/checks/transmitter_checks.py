from uuid import UUID

from app import models
from app import crud
from app.utils.exceptions import NameExistException, IdNotFoundException

__all__ = ['transmitter_is_exist']

crud_repo = crud.transmitter
model = models.Transmitter


async def transmitter_is_exist(id: UUID) -> None:
    obj = await crud_repo.get(id=id)
    if not obj:
        raise IdNotFoundException(model=model, id=id)
