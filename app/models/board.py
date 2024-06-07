from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel

__all__ = ['BaseBoard', 'Board', 'BoardUpdate']


class BaseBoard(SQLModel):

    name: str | None = None
    description: str | None = None
    address: str | None = Field(nullable=True)
    hardware_id: str | None = Field(nullable=True)


class BoardUpdate(BaseBoard):

    name: str | None = None
    description: str | None = None
    address: str | None = None
    hardware_id: str | None = None


class Board(BaseEntityModel, BaseBoard, table=True):

    __tablename__ = 'Board'
    __table_args__ = {'extend_existing': True}

    das: "DataAcquisitionSystem" = Relationship(
        back_populates='board',
        sa_relationship_kwargs={
            # "lazy": "joined",
            'uselist': False,
        }
    )