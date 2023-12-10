from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.sales_department import SalesDepartment
    from app.infrastructure.db.models.sales_department.manager_group import ManagerGroup


class Supervisor(Base):
    __tablename__ = 'supervisor'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    sales_department_id: Mapped[int] = mapped_column(ForeignKey('sales_department.id'))
    manager_group_id: Mapped[int] = mapped_column(ForeignKey('manager_group.id'))

    sales_department: Mapped['SalesDepartment'] = relationship(
        back_populates='managers',
    )
    manager_group: Mapped['ManagerGroup'] = relationship(
        back_populates='supervisor',
    )
