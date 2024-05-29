from fastapi import APIRouter, status, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud
from app.api.user import dependencies as deps
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

obj_in_message = 'Data Acquisition System'

model = models.DataAcquisitionSystem
read_schema = schemas.IDASRead
read_schema_full = schemas.IDASFullRead
update_schema = schemas.IDASUpdate
create_schema = schemas.IDASCreate

crud_repo = crud.das
deps_from_path = deps.get_das_by_id_from_path


@router.get("/list")
async def read_das_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of data acquisition systems
    """
    response = await crud_repo.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/{id}")
async def get_das_by_id(
        current: model = Depends(
            deps_from_path
        ),
) -> IGetResponseBase[read_schema_full]:
    """
    Gets das by its id
    """
    return create_response(data=current)


@router.put("/{id}")
async def update_das_by_id(
        update: update_schema,
        current: model = Depends(
            deps_from_path
        ),
) -> IPutResponseBase[read_schema]:
    """
    Updates das by id
    """
    if update.board_id:
        await checks.board_is_exist(id=update.board_id)
    if update.sensor_id:
        await checks.sensor_is_exist(id=update.sensor_id)

    updated = await crud_repo.update(obj_current=current, obj_new=update)
    return create_response(data=updated, message='{} updated'.format(obj_in_message))


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_das(
        create: create_schema,
) -> IPostResponseBase[read_schema]:
    """
    Creates a new das
    """

    await checks.das_name_is_taken(name=create.name)

    if create.board_id:
        await checks.board_is_exist(id=create.board_id)

    if create.sensor_id:
        await checks.sensor_is_exist(id=create.sensor_id)

    created = await crud_repo.create(obj_in=create)
    return create_response(data=created, message='{} created'.format(obj_in_message))


@router.delete("/{id}")
async def remove_das(
        current: model = Depends(
            deps_from_path
        ),
) -> IDeleteResponseBase[read_schema]:
    """
    Deletes das by id
    """

    deleted = await crud_repo.remove(id=current.id)
    return create_response(data=deleted, message="{} removed".format(obj_in_message))
