from uuid import UUID
from fastapi import Query, Body, Path
from typing_extensions import Annotated

from app import crud
from app import models
from app.utils.exceptions import IdNotFoundException

__all__ = ['get_sensor_by_id_from_path', 'get_sensor_by_id_from_query']


async def get_sensor(id: UUID) -> models.Sensor:
    response = await crud.sensor.get(id=id)
    if not response:
        raise IdNotFoundException(model=models.Sensor, id=id)
    return response


async def get_sensor_by_id_from_path(
        id: Annotated[UUID, Path(description="The UUID id of the sensor")]
) -> models.Sensor:
    return await get_sensor(id=id)


async def get_sensor_by_id_from_query(
        id: Annotated[UUID, Query(description="The UUID id of the sensor")]
) -> models.Sensor:
    return await get_sensor(id=id)
