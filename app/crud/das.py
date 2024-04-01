from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.DataAcquisitionSystem
update_schema = schemas.IDASUpdate
create_schema = schemas.IDASCreate


class CRUDDataAcquisitionSystem(CRUDBase[model, create_schema, update_schema]):

    @session_manager
    async def get_by_name(
            self,
            name: str,
            session: AsyncSession | None = None
    ) -> model | None:
        response = await session.execute(
            select(self.model).where(self.model.name == name))
        return response.scalar_one_or_none()

    @session_manager
    async def get_by_hardware_id(
            self,
            hardware_id: str,
            session: AsyncSession | None = None
    ) -> model | None:
        response = await session.execute(
            select(self.model).where(self.model.hardware_id == hardware_id))
        return response.scalar_one_or_none()

    #todo returning model

das = CRUDDataAcquisitionSystem(model=model)
