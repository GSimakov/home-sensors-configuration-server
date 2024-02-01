from sqlmodel import SQLModel

from app.utils.base_model import BaseEntityModel


class BaseSensorType(SQLModel):
    name: str


class SensorTypeUpdate(BaseSensorType):
    name: str | None = None


class SensorType(BaseEntityModel, BaseSensorType, table=True):

    __tablename__ = 'SensorType'
    __table_args__ = {'extend_existing': True}


