from fastapi import APIRouter, Depends

from app import models
from app import crud
from app.api.das import dependencies as deps

router = APIRouter()

obj_in_message = 'Config'


@router.get("/delay/{hardware_id}")
async def get_delay_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets delay parameter by hardware id
    """
    return await crud.config.get_delay_by_id(id=current_das.config_id)


@router.get("/conf_url/{hardware_id}")
async def get_conf_service_url_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets configuration service URL parameter by hardware id
    """
    return await crud.config.get_conf_service_url_by_id(id=current_das.config_id)


@router.get("/data_url/{hardware_id}")
async def get_data_service_url_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets data service URL parameter by hardware id
    """
    return await crud.config.get_data_service_url_by_id(id=current_das.config_id)


@router.get("/password/{hardware_id}")
async def get_password_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets password parameter by hardware id
    """
    return await crud.config.get_password_by_id(id=current_das.config_id)


@router.get("/ssid/{hardware_id}")
async def get_ssid_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets ssid parameter by hardware id
    """
    return await crud.config.get_ssid_by_id(id=current_das.config_id)


@router.get("/state/{hardware_id}")
async def get_state_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets state parameter by hardware id
    """
    return await crud.config.get_delay_by_id(id=current_das.config_id)
