from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.users.client import Client


class KindEnum(Enum):
    premium = 'premium'
    light = 'light'


@dataclass
class Subscription:
    id: int
    kind: str
    price: Decimal
    client_id: int
    created_at: datetime
    client: 'Client'
