from fastapi import APIRouter, status, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud
from app.api.v1 import dependencies as deps

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
async def read_mt_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[schemas.IMeasurementTypeRead]:
    """
    Gets a paginated list of measurement types
    """
    response = await crud.measurement_type.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/{id}")
async def get_mt_by_id(
        current_mt: models.MeasurementType = Depends(
            deps.get_mt_by_id_from_path
        ),
) -> IGetResponseBase[schemas.IMeasurementTypeRead]:
    """
    Gets a measurement type by its id
    """
    return create_response(data=current_mt)


@router.put("/{id}")
async def update_mt_by_id(
        mt: schemas.IMeasurementTypeUpdate,
        current_mt: models.MeasurementType = Depends(
            deps.get_mt_by_id_from_path
        ),
) -> IPutResponseBase[schemas.IMeasurementTypeRead]:
    """
    Updates a measurement type by id
    """

    updated = await crud.sensor.update(obj_current=current_mt, obj_new=mt)
    return create_response(data=updated, message='Measurement type updated')


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_mt(
        mt: schemas.IMeasurementTypeCreate
) -> IPostResponseBase[schemas.IMeasurementTypeRead]:
    """
    Creates a new measurement type
    """
    created = await crud.measurement_type.create(obj_in=mt)
    return create_response(data=created, message='Measurement type created')


@router.delete("/{id}")
async def remove_mt(
        current_mt: models.MeasurementType = Depends(
            deps.get_mt_by_id_from_path
        ),
) -> IDeleteResponseBase[schemas.IMeasurementTypeRead]:
    """
    Deletes a measurement type by id
    """

    deleted = await crud.measurement_type.remove(id=current_mt.id)
    return create_response(data=deleted, message="Measurement type removed")
