from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.technical_support.chat import Chat
    from app.domain.models.users.client import Client


@dataclass
class Ticket:
    id: int
    client_id: int
    chat_id: int

    client: 'Client'
    chat: 'Chat'
