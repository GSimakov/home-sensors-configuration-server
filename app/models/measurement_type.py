from sqlmodel import SQLModel

from app.utils.base_model import BaseEntityModel


class BaseMeasurementType(SQLModel):
    unit: str


class MeasurementTypeUpdate(BaseMeasurementType):
    unit: str | None = None


class MeasurementType(BaseEntityModel, BaseMeasurementType, table=True):

    __tablename__ = 'MeasurementType'
    __table_args__ = {'extend_existing': True}


