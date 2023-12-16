from abc import ABC, abstractmethod
from typing import List

from app.domain.models.users.manager import Manager
from app.infrastructure.database.interfaces.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class ManagerRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_active_managers(self) -> List[Manager]:
        raise NotImplementedError

    @abstractmethod
    async def get_manager_by_id(
        self,
        client_id: int,
    ) -> Manager:
        raise NotImplementedError
