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

obj_in_message = 'Data Acquisition System'

model = models.DataAcquisitionSystem
read_schema = schemas.IDASRead
update_schema = schemas.IDASUpdate
create_schema = schemas.IDASCreate

crud_das = crud.das
deps_from_path = deps.get_das_by_id_from_path


@router.post("", status_code=status.HTTP_201_CREATED)
async def register_das(
        hardware_id: str,
        request: Request
):
    """
    Register a new das
    """
    das_ip_addr = request.client.host

    await checks.das_hardware_id_is_taken(hardware_id=hardware_id)
    new_das = create_schema(hardware_id=hardware_id)
    await crud_das.create(obj_in=new_das)

    return 0


@router.delete("/{id}")
async def unregister_das(
        current: model = Depends(
            deps_from_path
        ),
) -> IDeleteResponseBase[read_schema]:
    """
    Unregister das by id
    """

    deleted = await crud_repo.remove(id=current.id)
    return create_response(data=deleted, message="{} removed".format(obj_in_message))
