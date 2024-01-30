from uuid import UUID
from sqlmodel import SQLModel

from app.utils.partial import optional
from app.models.test import BaseUser


class IUserCreate(BaseUser):
    pass


@optional
class IUserUpdate(BaseUser):
    pass


class IUserRead(BaseUser):
    id: UUID

