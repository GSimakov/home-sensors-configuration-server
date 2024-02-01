from uuid import UUID
from app import models


class ITransmitterCreate(models.BaseTransmitter):
    pass


class ITransmitterUpdate(models.TransmitterUpdate):
    pass


class ITransmitterRead(models.BaseTransmitter):
    id: UUID

