from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base

if TYPE_CHECKING:
    from app.infrastructure.database.models.users.client import Client


class KindEnum(Enum):
    premium = 'premium'
    light = 'light'


class Subscription(Base):
    __tablename__ = 'subscription'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    kind: Mapped[Enum] = mapped_column(String)
    price: Mapped[Decimal]
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
    )

    client: Mapped['Client'] = relationship(
        back_populates='subscriptions',
    )
