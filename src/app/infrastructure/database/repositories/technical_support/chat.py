from typing import List

from sqlalchemy import select

from app.domain.models.technical_support.chat import Chat, Message
from app.infrastructure.database.interfaces.repositories.technical_support.chat import (
    ChatRepositoryInterface,
)
from app.infrastructure.database.models.technical_support.chat import Chat as ChatDB
from app.infrastructure.database.models.technical_support.chat import (
    Message as MessageDB,
)


class ChatRepository(ChatRepositoryInterface):
    async def get_chats_for_client(
        self,
        client_id: int,
    ) -> List[Chat]:
        query = select(ChatDB).where(ChatDB.client_id == client_id)
        result = (await self._session.execute(query)).scalars().all()
        return result

    # todo: need implement limit and offset
    async def get_messages_for_chat(
        self,
        chat_id: int,
    ) -> Message:
        query = select(MessageDB).where(MessageDB.chat_id == chat_id)
        result = (await self._session.execute(query)).scalar()
        return result
