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
async def read_sensor_types_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[schemas.ISensorTypeRead]:
    """
    Gets a paginated list of sensor types
    """
    response = await crud.sensor_type.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/{id}")
async def get_sensor_type_by_id(
        current_sensor_type: models.SensorType = Depends(
            deps.get_sensor_type_by_id_from_path
        ),
) -> IGetResponseBase[schemas.ISensorTypeRead]:
    """
    Gets a sensor type by its id
    """
    return create_response(data=current_sensor_type)


@router.put("/{id}")
async def update_sensor_type_by_id(
        sensor_type: schemas.ISensorTypeUpdate,
        current_sensor_type: models.SensorType = Depends(
            deps.get_sensor_type_by_id_from_path
        ),
) -> IPutResponseBase[schemas.ISensorTypeRead]:
    """
    Updates a sensor type by id
    """
    updated = await crud.sensor_type.update(obj_current=current_sensor_type, obj_new=sensor_type)
    return create_response(data=updated, message='Sensor type updated')


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_sensor_type(
        sensor_type: schemas.ISensorTypeCreate
) -> IPostResponseBase[schemas.ISensorTypeRead]:
    """
    Creates a new sensor
    """

    created = await crud.sensor_type.create(obj_in=sensor_type)
    return create_response(data=created, message='Sensor type created')


@router.delete("/{id}")
async def remove_sensor_type(
        current_sensor_type: models.SensorType = Depends(
            deps.get_sensor_type_by_id_from_path
        ),
) -> IDeleteResponseBase[schemas.ISensorTypeRead]:
    """
    Deletes a sensor by id
    """

    deleted = await crud.sensor_type.remove(id=current_sensor_type.id)
    return create_response(data=deleted, message="Sensor type removed")
