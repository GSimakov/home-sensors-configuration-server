from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from app.utils.base_model import BaseEntityModel


class BaseJournalDAS(SQLModel):
    DAS_id: UUID = Field(foreign_key="DataAcquisitionSystem.id")
    event: str
    status: str | None = None


class JournalDAS(BaseEntityModel, BaseJournalDAS, table=True):

    __tablename__ = 'JournalDAS'
    __table_args__ = {'extend_existing': True}

    das: "DataAcquisitionSystem" = Relationship(
        back_populates='journal',
        sa_relationship_kwargs={
            "lazy": "joined",
            'primaryjoin': 'JournalDAS.DAS_id==DataAcquisitionSystem.id'
        }
    )

