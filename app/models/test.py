from uuid import UUID
from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy_utils.types.encrypted.encrypted_type import EncryptedType
from sqlalchemy import String

from app.core.settings import settings
from app.models.base import BaseEntityModel


class BaseUser(SQLModel):
    name: str = Field(sa_column=Column(EncryptedType(String, settings.SECRET_KEY), nullable=False))
    password: str = Field(sa_column=Column(EncryptedType(String, settings.SECRET_KEY), nullable=False))


class User(BaseUser, BaseEntityModel, table=True):

    __tablename__ = "User"
    __table_args__ = {'extend_existing': True}


