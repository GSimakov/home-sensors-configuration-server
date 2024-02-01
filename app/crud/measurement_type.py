from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models


class CRUDMeasurementType(
    CRUDBase[
        models.MeasurementType,
        schemas.IMeasurementTypeCreate,
        schemas.IMeasurementTypeUpdate
    ]
):

    async def get_by_name(
            self,
            name: str,
            session: AsyncSession | None = None
    ) -> models.MeasurementType | None:
        response = await session.execute(
            select(self.model).where(self.model.name == name))
        return response.scalar_one_or_none()


measurement_type = CRUDMeasurementType(model=models.MeasurementType)
