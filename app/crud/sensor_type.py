from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

class CRUDSensorType(CRUDBase[models.SensorType, schemas.ISensorTypeCreate, schemas.ISensorTypeUpdate]):

    @session_manager
    async def get_by_name(
            self,
            name: str,
            session: AsyncSession | None = None
    ) -> models.SensorType | None:
        response = await session.execute(
            select(self.model).where(self.model.name == name))
        return response.scalar_one_or_none()


sensor_type = CRUDSensorType(model=models.SensorType)
