from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.domain.models.users.manager import Manager
    from app.domain.models.users.supervisor import Supervisor


@dataclass
class ManagerGroup:
    id: int
    supervisor_id: int

    supervisor: Supervisor
    managers: List[Manager] = field(default_factory=list)
