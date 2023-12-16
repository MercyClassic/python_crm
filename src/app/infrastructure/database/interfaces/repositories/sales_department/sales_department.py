from abc import ABC, abstractmethod
from typing import List

from app.domain.models.sales_department.sales_department import SalesDepartment
from app.infrastructure.database.interfaces.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class SalesDepartmentRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_sales_departments(self) -> List[SalesDepartment]:
        raise NotImplementedError
