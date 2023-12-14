from abc import ABC, abstractmethod
from typing import List

from app.domain.models.tasks.manager_task import ManagerTask
from app.infrastructure.common.database.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class ManagerTaskRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    # todo: add filters against many functions
    @abstractmethod
    async def get_manager_tasks_for_manager(
        self,
        manager_id: int,
    ) -> List[ManagerTask]:
        raise NotImplementedError

    @abstractmethod
    async def get_manager_tasks_for_supervisor(
        self,
        supervisor_id: int,
    ) -> List[ManagerTask]:
        raise NotImplementedError

    @abstractmethod
    async def get_expired_manager_tasks_for_manager(
        self,
        manager_id: int,
    ) -> List[ManagerTask]:
        raise NotImplementedError

    @abstractmethod
    async def get_expired_manager_tasks_for_supervisor(
        self,
        supervisor_id: int,
    ) -> List[ManagerTask]:
        raise NotImplementedError

    @abstractmethod
    async def get_active_manager_tasks_for_manager(
        self,
        manager_id: int,
    ) -> List[ManagerTask]:
        raise NotImplementedError

    @abstractmethod
    async def get_active_manager_tasks_for_supervisor(
        self,
        supervisor_id: int,
    ) -> List[ManagerTask]:
        raise NotImplementedError

    @abstractmethod
    async def get_manager_task_by_id(
        self,
        task_id: int,
    ) -> ManagerTask:
        raise NotImplementedError
