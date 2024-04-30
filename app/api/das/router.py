from fastapi import APIRouter

from app.api.das.endpoints import registration
from app.api.das.endpoints import config, measurement


api_router_das = APIRouter()
api_router_das.include_router(registration.router, prefix="/reg", tags=["Registration"])
api_router_das.include_router(config.router, prefix="/config", tags=["Config"])
api_router_das.include_router(measurement.router, prefix="/measurement_type", tags=["MeasurementType"])
