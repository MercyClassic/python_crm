from typing import List

from sqlalchemy import select

from app.domain.models.users.supervisor import Supervisor
from app.infrastructure.database.interfaces.repositories.users.supervisor import (
    SupervisorRepositoryInterface,
)
from app.infrastructure.database.models.users.supervisor import (
    Supervisor as SupervisorDB,
)


class SupervisorRepository(SupervisorRepositoryInterface):
    async def get_active_supervisors(self) -> List[Supervisor]:
        query = select(SupervisorDB).where(SupervisorDB.is_active.is_(True))
        result = (await self._session.execute(query)).scalars().all()
        return result

    async def get_supervisor_by_id(
        self,
        client_id: int,
    ) -> Supervisor:
        query = select(SupervisorDB).where(SupervisorDB.id == client_id)
        result = (await self._session.execute(query)).scalar()
        return result
