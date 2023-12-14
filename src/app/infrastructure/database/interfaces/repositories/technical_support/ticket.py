from abc import ABC, abstractmethod
from typing import List

from app.domain.models.technical_support.ticket import Ticket
from app.infrastructure.common.database.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class TicketRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_tickets_for_client(
        self,
        client_id: int,
    ) -> List[Ticket]:
        raise NotImplementedError
