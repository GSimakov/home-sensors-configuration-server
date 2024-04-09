from fastapi import APIRouter, status, Request

from app import schemas
from app import models
from app import crud
from app.api.user import dependencies as deps
from app.utils.registration import register, unregister

router = APIRouter()

obj_in_message = 'Data Acquisition System'

model = models.DataAcquisitionSystem
read_schema = schemas.IDASRead
update_schema = schemas.IDASUpdate
create_schema = schemas.IDASCreate

crud_repo = crud.das
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
    await register(hardware_id=hardware_id, addr=das_ip_addr)


#todo cascade delete
@router.delete("", status_code=status.HTTP_200_OK)
async def prohibit_registration(hardware_id: str):
    """
    Unregister das by id
    """
    await unregister(hardware_id=hardware_id)

