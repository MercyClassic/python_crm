from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.users.client import Client


class Ticket(Base):
    __tablename__ = 'ticket'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    problem: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    opened_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
    )
    close_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=True,
    )

    client: Mapped['Client'] = relationship(
        back_populates='tickets',
    )
