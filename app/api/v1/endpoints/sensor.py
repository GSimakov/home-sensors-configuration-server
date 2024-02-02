from fastapi import APIRouter, status, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud
from app.api.v1 import dependencies as deps
from app.utils import checks

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()


@router.get("/list")
async def read_sensors_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[schemas.ISensorRead]:
    """
    Gets a paginated list of sensors
    """
    response = await crud.sensor.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/{id}")
async def get_sensor_by_id(
        current_sensor: models.Sensor = Depends(
            deps.get_sensor_by_id_from_path
        ),
) -> IGetResponseBase[schemas.ISensorRead]:
    """
    Gets a sensor by its id
    """
    return create_response(data=current_sensor)


@router.put("/{id}")
async def update_sensor_by_id(
        sensor: schemas.ISensorUpdate,
        current_sensor: models.Sensor = Depends(
            deps.get_sensor_by_id_from_path
        ),
) -> IPutResponseBase[schemas.ISensorRead]:
    """
    Updates a sensor by id
    """
    if sensor.transmitter_id:
        await checks.transmitter_is_exist(id=sensor.transmitter_id)
    if sensor.type_id:
        await checks.sensor_type_is_exist(id=sensor.type_id)
    if sensor.measurement_type_id:
        await checks.measurements_type_is_exist(id=sensor.measurement_type_id)

    updated = await crud.sensor.update(obj_current=current_sensor, obj_new=sensor)
    return create_response(data=updated, message='Sensor updated')


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_sensor(
        sensor: schemas.ISensorCreate
) -> IPostResponseBase[schemas.ISensorRead]:
    """
    Creates a new sensor
    """
    if sensor.transmitter_id:
        await checks.transmitter_is_exist(id=sensor.transmitter_id)
    if sensor.type_id:
        await checks.sensor_type_is_exist(id=sensor.type_id)
    if sensor.measurement_type_id:
        await checks.measurements_type_is_exist(id=sensor.measurement_type_id)

    created = await crud.sensor.create(obj_in=sensor)
    return create_response(data=created, message='Sensor created')


@router.delete("/{id}")
async def remove_sensor(
        current_sensor: models.Sensor = Depends(
            deps.get_sensor_by_id_from_path
        ),
) -> IDeleteResponseBase[schemas.ISensorRead]:
    """
    Deletes a sensor by id
    """

    deleted = await crud.sensor.remove(id=current_sensor.id)
    return create_response(data=deleted, message="Sensor removed")