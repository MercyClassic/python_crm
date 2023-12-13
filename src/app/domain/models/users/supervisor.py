from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.domain.models.sales_department import SalesDepartment
    from app.domain.models.sales_department.manager_group import ManagerGroup
    from app.domain.models.tasks.manager_task import ManagerTask


@dataclass
class Supervisor:
    id: int
    name: str
    sales_department_id: int
    manager_group_id: int

    sales_department: SalesDepartment
    manager_group: ManagerGroup
    delegated_tasks: List[ManagerTask]
