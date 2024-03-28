from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel


class BaseSensor(SQLModel):
    name: str
    type: str
    measurement_type_id: UUID | None = Field(
        default=None, foreign_key="MeasurementType.id"
    )


class SensorUpdate(BaseSensor):
    name: str | None = None
    type: str | None = None
    measurement_type_id: UUID | None = None


class Sensor(BaseEntityModel, BaseSensor, table=True):

    __tablename__ = 'Sensor'
    __table_args__ = {'extend_existing': True}

    #todo many them one sensor on board?
    das: "DataAcquisitionSystem" = Relationship(
        back_populates='sensor',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "DataAcquisitionSystem.sensor_id",
        }
    )

    measurement_type: "MeasurementType" = Relationship(
        back_populates='sensors',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "primaryjoin": "Sensor.measurement_type_id==MeasurementType.id",
        }
    )
