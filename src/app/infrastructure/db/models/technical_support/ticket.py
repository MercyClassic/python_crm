from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.technical_support.chat import Chat
    from app.infrastructure.db.models.users.client import Client


class Ticket(Base):
    __tablename__ = 'ticket'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))

    client: Mapped['Client'] = relationship(
        back_populates='tickets',
    )
    chat: Mapped['Chat'] = relationship(
        back_populates='ticket',
    )
