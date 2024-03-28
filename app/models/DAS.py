from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel


class BaseDataAcquisitionSystem(SQLModel):

    name: str | None = Field(nullable=True)

    board_id: UUID | None = Field(
        default=None, foreign_key="Board.id"
    )

    transmitter_id: UUID | None = Field(
        default=None, foreign_key="Transmitter.id"
    )

    sensor_id: UUID | None = Field(
        default=None, foreign_key="Sensor.id"
    )


class DataAcquisitionSystemUpdate(BaseDataAcquisitionSystem):
    hardware_id: UUID
    name: str | None = None
    transmitter_id: UUID | None = None
    sensor_id: UUID | None = None
    board_id: UUID | None


class DataAcquisitionSystem(BaseEntityModel, BaseDataAcquisitionSystem, table=True):

    __tablename__ = 'DataAcquisitionSystem'
    __table_args__ = {'extend_existing': True}


    sensor: "Sensor" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "DataAcquisitionSystem.sensor_id==Sensor.id",
        }
    )

    transmitter: "Transmitter" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "DataAcquisitionSystem.transmitter_id==Transmitter.id",
        }
    )

    board: "Board" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "DataAcquisitionSystem.board_id==Board.id",
        }
    )
