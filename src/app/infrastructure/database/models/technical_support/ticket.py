from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.technical_support.chat import Chat
    from app.infrastructure.database.models.users.client import Client


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
