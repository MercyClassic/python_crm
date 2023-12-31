from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.technical_support.ticket import Ticket
    from app.infrastructure.database.models.users.client import Client
    from app.infrastructure.database.models.users.manager import Manager


class Chat(Base):
    __tablename__ = 'chat'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))

    client: Mapped['Client'] = relationship(
        back_populates='chats',
    )


class Message(Base):
    __tablename__ = 'message'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    manager_id: Mapped[int] = mapped_column(ForeignKey('manager.id'))
    text: Mapped[str]
    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
    )
    is_read: Mapped[bool] = mapped_column(default=False)

    chat: Mapped['Chat'] = relationship(
        backref='messages',
    )
    client: Mapped['Client'] = relationship(
        backref='messages',
    )
    manager: Mapped['Manager'] = relationship(
        backref='messages',
    )
