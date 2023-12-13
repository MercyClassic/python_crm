from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.database import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.users.client import Client


class KindEnum(Enum):
    premium = 'premium'
    light = 'light'


class Subscription(Base):
    __tablename__ = 'subscription'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    kind: Mapped[ENUM] = mapped_column(
        ENUM(
            KindEnum,
            name='subscription_kind',
        ),
    )
    price: Mapped[Decimal]
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    client: Mapped['Client'] = relationship(
        back_populates='subscriptions',
    )
