from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID
from app.crud.base import CRUDBase


from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Config
update_schema = schemas.IConfigUpdate
create_schema = schemas.IConfigCreate


class CRUDConfig(CRUDBase[model, create_schema, update_schema]):

    @session_manager
    async def get_delay_by_id(
            self,
            id: UUID,
            session: AsyncSession | None = None
    ) -> str:
        response = await session.execute(
            select(self.model.delay).where(self.model.id == id))
        return response.scalar_one_or_none()

    @session_manager
    async def get_ssid_by_id(
            self,
            id: UUID,
            session: AsyncSession | None = None
    ) -> str:
        response = await session.execute(
            select(self.model.ssid).where(self.model.id == id))
        return response.scalar_one_or_none()

    @session_manager
    async def get_password_by_id(
            self,
            id: UUID,
            session: AsyncSession | None = None
    ) -> str:
        response = await session.execute(
            select(self.model.password).where(self.model.id == id))
        return response.scalar_one_or_none()

    @session_manager
    async def get_server_url_by_id(
            self,
            id: UUID,
            session: AsyncSession | None = None
    ) -> str:
        response = await session.execute(
            select(self.model.serverURL).where(self.model.id == id))
        return response.scalar_one_or_none()


config = CRUDConfig(model=model)
