from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.technical_support.ticket import Ticket
    from app.infrastructure.db.models.users.client import Client
    from app.infrastructure.db.models.users.manager import Manager


class Chat(Base):
    __tablename__ = 'chat'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    ticket_id: Mapped[int] = mapped_column(ForeignKey('ticket.id'))

    client: Mapped['Client'] = relationship(
        back_populates='chats',
    )
    ticket: Mapped['Ticket'] = relationship(
        back_populates='chat',
    )


class Message(Base):
    __tablename__ = 'message'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    manager_id: Mapped[int] = mapped_column(ForeignKey('manager.id'))
    text: Mapped[str]

    chat: Mapped['Chat'] = relationship(
        backref='messages',
    )
    client: Mapped['Client'] = relationship(
        backref='messages',
    )
    manager: Mapped['Manager'] = relationship(
        backref='messages',
    )
