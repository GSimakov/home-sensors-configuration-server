from sqlmodel import SQLModel, Relationship

from app.utils.base_model import BaseEntityModel

__all__ = ['BaseMeasurementType', 'MeasurementType', 'MeasurementTypeUpdate']


class BaseMeasurementType(SQLModel):
    name: str
    unit: str


class MeasurementTypeUpdate(BaseMeasurementType):
    name: str | None = None
    unit: str | None = None



class MeasurementType(BaseEntityModel, BaseMeasurementType, table=True):

    __tablename__ = 'MeasurementType'
    __table_args__ = {'extend_existing': True}

    sensors: list["Sensor"] = Relationship(
        back_populates='measurement_type',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Sensor.measurement_type_id",
        }
    )
