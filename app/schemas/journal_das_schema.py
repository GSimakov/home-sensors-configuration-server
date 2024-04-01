from uuid import UUID
from app import models
from datetime import datetime

__all__ = ['IJournalDASCreate', 'IJournalDASRead']

base_model = models.BaseJournalDAS


class IJournalDASCreate(base_model):
    pass


class IJournalDASRead(base_model):
    id: UUID
    created_at: datetime



