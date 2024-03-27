from uuid import UUID
from app import models


class IBoardCreate(models.BaseBoard):
    pass


class IBoardUpdate(models.BaseBoard):
    pass


class IBoardRead(models.BaseBoard):
    id: UUID

