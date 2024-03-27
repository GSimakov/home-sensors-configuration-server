from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager


class CRUDBoard(CRUDBase[models.Board, schemas.IBoardCreate, schemas.IBoardUpdate]):

    @session_manager
    async def get_by_name(
            self,
            name: str,
            session: AsyncSession | None = None
    ) -> models.Board | None:
        response = await session.execute(
            select(self.model).where(self.model.name == name))
        return response.scalar_one_or_none()


board = CRUDBoard(model=models.Board)
