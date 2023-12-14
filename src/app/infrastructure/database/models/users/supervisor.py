from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.sales_department import SalesDepartment
    from app.infrastructure.database.models.sales_department.manager_group import (
        ManagerGroup,
    )
    from app.infrastructure.database.models.tasks.manager_task import ManagerTask


class Supervisor(Base):
    __tablename__ = 'supervisor'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    is_active: Mapped[bool]
    sales_department_id: Mapped[int] = mapped_column(ForeignKey('sales_department.id'))
    manager_group_id: Mapped[int] = mapped_column(ForeignKey('manager_group.id'))

    sales_department: Mapped['SalesDepartment'] = relationship(
        back_populates='managers',
    )
    manager_group: Mapped['ManagerGroup'] = relationship(
        back_populates='supervisor',
    )
    delegated_tasks: Mapped[List['ManagerTask']] = relationship(
        back_populates='delegated_by',
    )
