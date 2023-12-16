from typing import List

from sqlalchemy import select

from app.domain.models.users.client import Client
from app.infrastructure.database.interfaces.repositories.users.client import (
    ClientRepositoryInterface,
)
from app.infrastructure.database.models.users.client import Client as ClientDB


class ClientRepository(ClientRepositoryInterface):
    async def get_active_clients(self) -> List[Client]:
        query = select(ClientDB).where(ClientDB.is_active.is_(True))
        result = (await self._session.execute(query)).scalars().all()
        return result

    async def get_client_by_id(
        self,
        client_id: int,
    ) -> Client:
        query = select(ClientDB).where(ClientDB.id == client_id)
        result = (await self._session.execute(query)).scalar()
        return result

    async def get_client_by_email(
        self,
        email: str,
    ) -> Client:
        query = select(ClientDB).where(ClientDB.email == email)
        result = (await self._session.execute(query)).scalar()
        return result
