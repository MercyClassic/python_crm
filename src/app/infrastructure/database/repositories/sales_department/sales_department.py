from typing import List

from sqlalchemy import select

from app.domain.models.sales_department.sales_department import SalesDepartment
from app.infrastructure.database.interfaces.repositories.sales_department.sales_department import (
    SalesDepartmentRepositoryInterface,
)
from app.infrastructure.database.models.sales_department.sales_department import (
    SalesDepartment as SalesDepartmentDB,
)


class SalesDepartmentRepository(SalesDepartmentRepositoryInterface):
    async def get_sales_departments(self) -> List[SalesDepartment]:
        query = select(SalesDepartmentDB)
        result = (await self._session.execute(query)).scalars().all()
        return result
