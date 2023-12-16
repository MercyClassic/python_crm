from typing import List

from sqlalchemy import select

from app.domain.models.technical_support.ticket import Ticket
from app.infrastructure.database.interfaces.repositories.technical_support.ticket import (
    TicketRepositoryInterface,
)
from app.infrastructure.database.models.technical_support.ticket import (
    Ticket as TicketDB,
)


class TicketRepository(TicketRepositoryInterface):
    async def get_tickets_for_client(
        self,
        client_id: int,
    ) -> List[Ticket]:
        query = select(TicketDB).where(TicketDB.client_id == client_id)
        result = (await self._session.execute(query)).scalars().all()
        return result
