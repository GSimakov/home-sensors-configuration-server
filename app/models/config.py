from uuid import UUID
from sqlalchemy import Column
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy_utils.types.url import URLType

from app.utils.base_model import BaseEntityModel

__all__ = ['BaseConfig', 'ConfigUpdate', 'Config']


class BaseConfig(SQLModel):
    ssid: str
    password: str
    confURL: str = Field(sa_column=Column(URLType))
    dataURL: str = Field(sa_column=Column(URLType))
    delay: int = 1000


class ConfigUpdate(BaseConfig):
    ssid: str | None = None
    password: str | None = None
    confURL: str = Field(sa_column=Column(URLType))
    dataURL: str = Field(sa_column=Column(URLType))
    delay: int | None = None


class Config(BaseEntityModel, BaseConfig, table=True):

    __tablename__ = 'Config'
    __table_args__ = {'extend_existing': True}

    dasList: list["DataAcquisitionSystem"] = Relationship(
        back_populates='config',
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "DataAcquisitionSystem.configId",
        }
    )
