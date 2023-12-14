from abc import ABC, abstractmethod
from typing import List

from app.domain.models.sales_department.manager_group import ManagerGroup
from app.infrastructure.common.database.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class ManagerGroupRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_manager_groups_for_supervisor(
        self,
        supervisor_id: int,
    ) -> List[ManagerGroup]:
        raise NotImplementedError
