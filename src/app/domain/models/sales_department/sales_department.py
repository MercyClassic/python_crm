from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.domain.models.users.supervisor import Supervisor


@dataclass
class SalesDepartment:
    id: int
    title: str

    supervisors: List[Supervisor] = field(default_factory=list)
