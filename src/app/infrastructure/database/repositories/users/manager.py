from typing import List

from sqlalchemy import select

from app.domain.models.users.manager import Manager
from app.infrastructure.database.interfaces.repositories.users.manager import (
    ManagerRepositoryInterface,
)
from app.infrastructure.database.models.users.manager import Manager as ManagerDB


class ManagerRepository(ManagerRepositoryInterface):
    async def get_active_managers(self) -> List[Manager]:
        query = select(ManagerDB).where(ManagerDB.is_active.is_(True))
        result = (await self._session.execute(query)).scalars().all()
        return result

    async def get_manager_by_id(
        self,
        client_id: int,
    ) -> Manager:
        query = select(ManagerDB).where(ManagerDB.id == client_id)
        result = (await self._session.execute(query)).scalar()
        return result
