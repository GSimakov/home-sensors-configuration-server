from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel


__all__ = ['BaseSensor', 'Sensor', 'SensorUpdate']


class BaseSensor(SQLModel):
    name: str
    type: str
    measurementTypeId: UUID | None = Field(
        default=None, foreign_key="MeasurementType.id"
    )


class SensorUpdate(BaseSensor):
    name: str | None = None
    type: str | None = None
    measurementTypeId: UUID | None = None


class Sensor(BaseEntityModel, BaseSensor, table=True):

    __tablename__ = 'Sensor'
    __table_args__ = {'extend_existing': True}

    #todo many them one sensor on board?
    das: "DataAcquisitionSystem" = Relationship(
        back_populates='sensor',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "DataAcquisitionSystem.sensorId",
        }
    )

    measurementType: "MeasurementType" = Relationship(
        back_populates='sensorsList',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "primaryjoin": "Sensor.measurementTypeId==MeasurementType.id",
        }
    )
