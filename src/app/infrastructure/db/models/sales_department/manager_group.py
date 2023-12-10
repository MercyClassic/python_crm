from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.users.manager import Manager
    from app.infrastructure.db.models.users.supervisor import Supervisor


class ManagerGroup(Base):
    __tablename__ = 'manager_group'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    supervisor_id: Mapped[int] = mapped_column(ForeignKey('supervisor.id'))

    supervisor: Mapped['Supervisor'] = relationship(
        back_populates='manager_group',
    )
    managers: Mapped[List['Manager']] = relationship(
        back_populates='manager_group',
    )
