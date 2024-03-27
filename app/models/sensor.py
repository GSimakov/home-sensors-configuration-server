from sqlmodel import SQLModel, Relationship

from app.utils.base_model import BaseEntityModel


class BaseSensor(SQLModel):
    name: str


class SensorUpdate(BaseSensor):
    name: str | None = None


class Sensor(BaseEntityModel, BaseSensor, table=True):

    __tablename__ = 'Sensor'
    __table_args__ = {'extend_existing': True}

    das: "DataAcquisitionSystem" = Relationship(
        back_populates='sensor',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "DataAcquisitionSystem.sensor_id",
        }
    )
