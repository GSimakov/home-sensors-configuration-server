from uuid import UUID

from app import models
from app import crud
from app.utils.exceptions import NameExistException, IdNotFoundException

__all__ = ['sensor_type_name_is_taken', 'sensor_type_is_exist']


async def sensor_type_name_is_taken(name: str) -> None:
    obj = await crud.sensor_type.get_by_name(name=name)
    if obj:
        raise NameExistException(model=models.SensorType, name=name)


async def sensor_type_is_exist(id: UUID) -> None:
    obj = await crud.sensor_type.get(id=id)
    if not obj:
        raise IdNotFoundException(model=models.SensorType, id=id)
