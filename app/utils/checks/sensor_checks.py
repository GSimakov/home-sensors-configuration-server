from uuid import UUID

from app import models
from app import crud
from app.utils.exceptions import NameExistException, IdNotFoundException

__all__ = ['sensor_is_exist']

crud_repo = crud.sensor
model = models.Sensor


async def sensor_is_exist(id: UUID) -> None:
    obj = await crud_repo.get(id=id)
    if not obj:
        raise IdNotFoundException(model=model, id=id)
