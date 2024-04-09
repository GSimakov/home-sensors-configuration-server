from fastapi import APIRouter

from app.api.das.endpoints import registration


api_router_das = APIRouter()
api_router_das.include_router(registration.router, prefix="/reg", tags=["Registration"])


