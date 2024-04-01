from app.crud.base import CRUDBase
from app import schemas
from app import models

model = models.JournalDAS
update_schema = None
create_schema = schemas.IJournalDASCreate


class CRUDJournalDAS(CRUDBase[model, create_schema, update_schema]):
    pass


journal_das = CRUDJournalDAS(model=model)
