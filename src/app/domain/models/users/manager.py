from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.domain.models.sales_department.manager_group import ManagerGroup
    from app.domain.models.tasks.manager_task import ManagerTask


@dataclass
class Manager:
    id: int
    name: str
    manager_group_id: int

    manager_group: ManagerGroup
    tasks: List[ManagerTask] = field(default_factory=list)
