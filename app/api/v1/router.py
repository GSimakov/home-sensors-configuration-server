from fastapi import APIRouter
from app.api.v1.endpoints import (sensor)


api_router_v1 = APIRouter()
api_router_v1.include_router(sensor.router, prefix="/sensor", tags=["Sensor"])
