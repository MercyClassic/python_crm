from abc import ABC, abstractmethod
from typing import List

from app.domain.models.users.client import Client
from app.infrastructure.common.database.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class ClientRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_active_clients(self) -> List[Client]:
        raise NotImplementedError

    @abstractmethod
    async def get_client_by_id(
        self,
        client_id: int,
    ) -> Client:
        raise NotImplementedError
