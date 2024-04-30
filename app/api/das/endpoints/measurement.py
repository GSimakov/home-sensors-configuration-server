from fastapi import APIRouter, Depends

from app import models
from app import crud
from app.api.das import dependencies as deps

router = APIRouter()


@router.get("/unit/{hardware_id}")
async def get_unit_by_hardware_id(
    current_das: models.DataAcquisitionSystem = Depends(
        deps.get_das_by_board_hardware_id_from_path
    ),
):
    """
    Gets unit of sensor measurements by board hardware id
    """
    current_sensor = await crud.sensor.get(id=current_das.sensor_id)
    current_measurement_type = await crud.measurement_type.get(id=current_sensor.measurement_type_id)
    unit = current_measurement_type.unit
    return unit