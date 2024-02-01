from uuid import UUID
from sqlmodel import SQLModel, Field

from app.utils.base_model import BaseEntityModel


class BaseSensor(SQLModel):

    name: str | None = Field(nullable=False)
    description: str | None = None

    transmitter_id: UUID | None = Field(
        default=None, foreign_key="Transmitter.id"
    )

    type_id: UUID | None = Field(
        default=None, foreign_key="SensorType.id"
    )

    measurement_type_id: UUID | None = Field(
        default=None, foreign_key="MeasurementType.id"
    )


class SensorUpdate(BaseSensor):
    name: str | None = None
    description: str | None = None
    MAC: str | None = None
    IP: str | None = None
    type: str | None = None
    measurement: str | None = None


class Sensor(BaseEntityModel, BaseSensor, table=True):

    __tablename__ = 'Sensor'
    __table_args__ = {'extend_existing': True}


