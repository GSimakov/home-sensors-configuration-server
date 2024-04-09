from fastapi import APIRouter

from app.api.user.endpoints import (
    config,
    journal_das,
    das,
    board,
    sensor,
    measurement_type
)

api_router_user = APIRouter()
api_router_user.include_router(config.router, prefix="/config", tags=["Config"])
api_router_user.include_router(journal_das.router, prefix="/journal", tags=["Journal"])
api_router_user.include_router(das.router, prefix="/DAS", tags=["DAS"])
api_router_user.include_router(board.router, prefix="/board", tags=["Board"])
api_router_user.include_router(sensor.router, prefix="/sensor", tags=["Sensor"])
api_router_user.include_router(measurement_type.router, prefix="/measurement_type", tags=["MeasurementType"])


