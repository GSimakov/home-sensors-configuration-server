from fastapi import APIRouter
from app.api.v1.endpoints.user_side import config, sensor, journal_das, board, measurement_type
from app.api.v1.endpoints.das_side import registration, das

api_router_v1 = APIRouter()
api_router_v1.include_router(config.router, prefix="/config", tags=["Config"])
api_router_v1.include_router(journal_das.router, prefix="/journal", tags=["Journal"])
api_router_v1.include_router(registration.router, prefix="/reg", tags=["Registration"])
api_router_v1.include_router(das.router, prefix="/DAS", tags=["DAS"])
api_router_v1.include_router(board.router, prefix="/board", tags=["Board"])
api_router_v1.include_router(sensor.router, prefix="/sensor", tags=["Sensor"])
api_router_v1.include_router(measurement_type.router, prefix="/measurement_type", tags=["MeasurementType"])


