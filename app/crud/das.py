from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager


class CRUDDataAcquisitionSystem(CRUDBase[models.DataAcquisitionSystem, schemas.IDASCreate, schemas.IDASUpdate]):

    @session_manager
    async def get_by_name(
            self,
            name: str,
            session: AsyncSession | None = None
    ) -> models.DataAcquisitionSystem | None:
        response = await session.execute(
            select(self.model).where(self.model.name == name))
        return response.scalar_one_or_none()

    @session_manager
    async def get_by_hardware_id(
            self,
            hardware_id: str,
            session: AsyncSession | None = None
    ) -> models.DataAcquisitionSystem | None:
        response = await session.execute(
            select(self.model).where(self.model.hardware_id == hardware_id))
        return response.scalar_one_or_none()


das = CRUDDataAcquisitionSystem(model=models.DataAcquisitionSystem)
