from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel


__all__ = ['BaseSensor', 'Sensor', 'SensorUpdate']


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

    das: "DataAcquisitionSystem" = Relationship(
        back_populates='sensor',
        sa_relationship_kwargs={
            'uselist': False
        }
    )

    measurement_type: "MeasurementType" = Relationship(
        back_populates='sensors_list',
        sa_relationship_kwargs={
            "primaryjoin": "Sensor.measurement_type_id==MeasurementType.id",
        }
    )
