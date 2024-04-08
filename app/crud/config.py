from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Config
update_schema = schemas.IConfigUpdate
create_schema = schemas.IConfigCreate


class CRUDConfig(CRUDBase[model, create_schema, update_schema]):
    pass


config = CRUDConfig(model=model)
