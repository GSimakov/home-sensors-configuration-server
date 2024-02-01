from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models


class CRUDTransmitter(
    CRUDBase[
        models.Transmitter,
        schemas.ITransmitterCreate,
        schemas.ITransmitterUpdate
    ]
):
    async def get_by_mac(
            self,
            mac: str,
            session: AsyncSession | None = None
    ) -> models.MeasurementType | None:
        response = await session.execute(
            select(self.model).where(self.model.MAC == mac))
        return response.scalar_one_or_none()\


    async def get_by_ip(
            self,
            ip: str,
            session: AsyncSession | None = None
    ) -> models.MeasurementType | None:
        response = await session.execute(
            select(self.model).where(self.model.IP == ip))
        return response.scalar_one_or_none()


transmitter = CRUDTransmitter(model=models.Transmitter)
