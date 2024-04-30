from uuid import UUID
from pydantic import BaseModel


class RegForm(BaseModel):
    hardware_id: str
