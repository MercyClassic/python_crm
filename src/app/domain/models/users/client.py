from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.domain.models.subscription.subscription import Subscription
    from app.domain.models.technical_support.ticket import Ticket


@dataclass
class Client:
    id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str

    tickets: List['Ticket'] = field(default_factory=list)
    subscriptions: List['Subscription'] = field(default_factory=list)
