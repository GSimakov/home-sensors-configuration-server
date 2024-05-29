import datetime
from pydantic import BaseModel
from uuid import UUID


from app import models
from app.schemas.board_schema import IBoardShortRead
from app.schemas.config_schema import IConfigShortRead
from app.schemas.sensor_schema import ISensorShortRead


__all__ = ['IDASCreate', 'IDASUpdate', 'IDASRead', 'IDASFullRead']

base_model = models.BaseDataAcquisitionSystem
update_model = models.DataAcquisitionSystemUpdate


class IDASCreate(base_model):
    pass


class IDASUpdate(update_model):
    pass


class IDASRead(base_model):
    id: UUID
    created_at: datetime.datetime


class IDASFullRead(BaseModel):
    id: UUID
    board: IBoardShortRead
    config: IConfigShortRead
    sensor: ISensorShortRead
    created_at: datetime.datetime