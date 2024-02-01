from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy_utils.types.ip_address import IPAddressType

from app.utils.base_model import BaseEntityModel


class BaseTransmitter(SQLModel):

    IP: str = Field(sa_column=Column(IPAddressType, nullable=False))
    MAC: str


class TransmitterUpdate(BaseTransmitter):
    IP: str | None = None
    MAC: str | None = None


class Transmitter(BaseEntityModel, BaseTransmitter, table=True):

    __tablename__ = 'Transmitter'
    __table_args__ = {'extend_existing': True}


    sensor: "Sensor" = Relationship(
        back_populates='transmitter',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Sensor.transmitter_id",
        }
    )
