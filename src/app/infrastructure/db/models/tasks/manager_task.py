from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.users.manager import Manager
    from app.infrastructure.db.models.users.supervisor import Supervisor


class ManagerTask(Base):
    __tablename__ = 'manager_task'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    delegated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    done_at: Mapped[datetime] = mapped_column(nullable=True)
    manager_id: Mapped[int] = mapped_column(ForeignKey('manager.id'))
    delegated_by_id: Mapped[int] = mapped_column(ForeignKey('supervisor.id'))

    manager: Mapped['Manager'] = relationship(
        back_populates='tasks',
    )
    delegated_by: Mapped['Supervisor'] = relationship(
        back_populates='delegated_tasks',
    )