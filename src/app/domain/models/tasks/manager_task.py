from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.users.manager import Manager
    from app.domain.models.users.supervisor import Supervisor


@dataclass
class ManagerTask:
    id: int
    title: str
    description: str
    delegated_at: datetime
    done_at: datetime | None = None
    manager_id: int
    delegated_by_id: int

    manager: Manager
    delegated_by: Supervisor
