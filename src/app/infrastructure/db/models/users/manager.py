from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.sales_department.manager_group import ManagerGroup
    from app.infrastructure.db.models.tasks.manager_task import ManagerTask


class Manager(Base):
    __tablename__ = 'manager'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    manager_group_id: Mapped[int] = mapped_column(ForeignKey('manager_group.id'))

    manager_group: Mapped['ManagerGroup'] = relationship(
        back_populates='managers',
    )
    tasks: Mapped[List['ManagerTask']] = relationship(
        back_populates='manager',
    )
