from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Sensor
update_schema = schemas.ISensorUpdate
create_schema = schemas.ISensorCreate


class CRUDSensor(CRUDBase[model, create_schema, update_schema]):

    @session_manager
    async def get_by_name(
            self,
            name: str,
            session: AsyncSession | None = None
    ) -> models.Sensor | None:
        response = await session.execute(
            select(self.model).where(self.model.name == name))
        return response.scalar_one_or_none()


sensor = CRUDSensor(model=model)
