from typing import TYPE_CHECKING, List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.subscription.subscription import (
        Subscription,
    )
    from app.infrastructure.database.models.technical_support.ticket import Chat, Ticket


class Client(Base):
    __tablename__ = 'client'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(300), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)

    tickets: Mapped[List['Ticket']] = relationship(
        back_populates='client',
    )
    chats: Mapped[List['Chat']] = relationship(
        back_populates='client',
    )
    subscriptions: Mapped[List['Subscription']] = relationship(
        back_populates='client',
    )
