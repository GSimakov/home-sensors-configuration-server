from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel

__all__ = ['BaseBoard', 'Board', 'BoardUpdate']


class BaseBoard(SQLModel):

    name: str | None = Field(nullable=True)
    description: str | None = Field(nullable=True)
    address: str | None = Field(nullable=True)
    hardwareId: str | None = Field(nullable=True)


class BoardUpdate(BaseBoard):

    name: str | None = None
    description: str | None
    address: str | None = Field(nullable=True)
    hardwareId: str | None = Field(nullable=True)


class Board(BaseEntityModel, BaseBoard, table=True):

    __tablename__ = 'Board'
    __table_args__ = {'extend_existing': True}

    das: "DataAcquisitionSystem" = Relationship(
        back_populates='board',
        sa_relationship_kwargs={
            "lazy": "joined",
            "foreign_keys": "DataAcquisitionSystem.boardId",
        }
    )