from fastapi import APIRouter, status, Depends, Request
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

obj_in_message = 'Config'

model = models.Config
read_schema = schemas.IConfigRead
update_schema = schemas.IConfigUpdate
create_schema = schemas.IDASCreate

crud_repo = crud.config
deps_from_path = deps.get_config_by_id_from_path


@router.get("/list")
async def read_configs_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of configs
    """
    response = await crud_repo.get_multi_paginated(params=params)
    return create_response(data=response)
