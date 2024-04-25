from uuid import UUID
from sqlalchemy import Column
from sqlalchemy_utils import IPAddressType
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel

__all__ = ['BaseDataAcquisitionSystem', 'DataAcquisitionSystem', 'DataAcquisitionSystemUpdate']


class BaseDataAcquisitionSystem(SQLModel):

    name: str | None = None
    hardware_id: str = Field(nullable=False)

    address: str = Field(nullable=False)

    board_id: UUID | None = Field(
        default=None, foreign_key="Board.id"
    )

    sensor_id: UUID | None = Field(
        default=None, foreign_key="Sensor.id"
    )

    config_id: UUID | None = Field(
        default=None, foreign_key="Config.id"
    )


class DataAcquisitionSystemUpdate(BaseDataAcquisitionSystem):
    name: str | None = None
    sensorId: UUID | None = None
    boardId: UUID | None = None
    configId: UUID | None = None


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

    board: "Board" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "DataAcquisitionSystem.board_id==Board.id",
        }
    )

    journal: list["JournalDAS"] = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            "lazy": "selectin",
            'foreign_keys': 'JournalDAS.DASId',
        }
    )

    config: "Config" = Relationship(
        back_populates='dasList',
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "DataAcquisitionSystem.configId==Config.id",
        }
    )
