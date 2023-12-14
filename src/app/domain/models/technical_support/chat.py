from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.technical_support.ticket import Ticket
    from app.domain.models.users.client import Client
    from app.domain.models.users.manager import Manager


@dataclass
class Chat:
    id: int
    client_id: int
    ticket_id: int

    client: 'Client'
    ticket: 'Ticket'


@dataclass
class Message:
    id: int
    chat_id: int
    client_id: int
    manager_id: int
    text: str

    chat: 'Chat'
    client: 'Client'
    manager: 'Manager'
