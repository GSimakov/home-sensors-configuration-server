from uuid import UUID
from sqlalchemy import Column
from sqlalchemy_utils import IPAddressType
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel

__all__ = ['BaseDataAcquisitionSystem', 'DataAcquisitionSystem', 'DataAcquisitionSystemUpdate']


class BaseDataAcquisitionSystem(SQLModel):

    name: str | None = None

    board_id: UUID | None = Field(
        default=None, foreign_key="Board.id"
    )

    sensor_id: UUID | None = Field(
        default=None, foreign_key="Sensor.id"
    )

    config_id: UUID | None = Field(
        default=None, foreign_key="Config.id"
    )

    state: bool = False


class DataAcquisitionSystemUpdate(BaseDataAcquisitionSystem):
    name: str | None = None
    sensor_id: UUID | None = None
    board_id: UUID | None = None
    config_id: UUID | None = None
    state: bool | None = None


class DataAcquisitionSystem(BaseEntityModel, BaseDataAcquisitionSystem, table=True):

    __tablename__ = 'DataAcquisitionSystem'
    __table_args__ = {'extend_existing': True}

    sensor: "Sensor" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            "primaryjoin": "DataAcquisitionSystem.sensor_id==Sensor.id",
        }
    )

    board: "Board" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            'primaryjoin': 'DataAcquisitionSystem.board_id==Board.id',
        }
    )

    journal: "JournalDAS" = Relationship(
        back_populates='das',
        sa_relationship_kwargs={
            'foreign_keys': 'JournalDAS.DAS_id',
        }
    )

    config: "Config" = Relationship(
        back_populates='das_list',
        sa_relationship_kwargs={
            "primaryjoin": "DataAcquisitionSystem.config_id==Config.id",
        }
    )
