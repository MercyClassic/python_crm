from typing import List

from sqlalchemy import select

from app.domain.models.sales_department.manager_group import (
    ManagerGroup as ManagerGroup,
)
from app.infrastructure.database.interfaces.repositories.sales_department.manager_group import (
    ManagerGroupRepositoryInterface,
)
from app.infrastructure.database.models.sales_department.manager_group import (
    ManagerGroup as ManagerGroupDB,
)


class ManagerGroupRepository(ManagerGroupRepositoryInterface):
    async def get_manager_groups_for_supervisor(
        self,
        supervisor_id: int,
    ) -> List[ManagerGroupDB]:
        query = select(ManagerGroupDB).where(supervisor_id=supervisor_id)
        result = (await self._session.execute(query)).scalars().all()
        return result
