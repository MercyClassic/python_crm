from abc import ABC, abstractmethod
from typing import List

from app.domain.models.technical_support.chat import Chat
from app.infrastructure.database.interfaces.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class ChatRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    @abstractmethod
    async def get_chats_for_client(
        self,
        client_id: int,
    ) -> List[Chat]:
        raise NotImplementedError

    # todo: need implement limit and offset
    @abstractmethod
    async def get_messages_for_chat(
        self,
        chat_id: int,
    ) -> Chat:
        raise NotImplementedError
