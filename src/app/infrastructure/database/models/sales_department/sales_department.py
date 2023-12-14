from typing import TYPE_CHECKING, List

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.users.supervisor import Supervisor


class SalesDepartment(Base):
    __tablename__ = 'sales_department'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]

    supervisors: Mapped[List['Supervisor']] = relationship(
        back_populates='sales_department',
    )
