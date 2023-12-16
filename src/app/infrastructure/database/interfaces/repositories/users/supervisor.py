from abc import ABC, abstractmethod
from typing import List

from app.domain.models.users.supervisor import Supervisor
from app.infrastructure.database.interfaces.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class SupervisorRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_active_supervisors(self) -> List[Supervisor]:
        raise NotImplementedError

    @abstractmethod
    async def get_supervisor_by_id(
        self,
        supervisor_id: int,
    ) -> Supervisor:
        raise NotImplementedError
