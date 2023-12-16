from abc import ABC, abstractmethod
from typing import List

from app.domain.models.subscription.subscription import Subscription
from app.infrastructure.database.interfaces.repositories.sqlaclhemy_gateway import (
    SQLAlchemyBaseGateway,
)


class SubscriptionRepositoryInterface(SQLAlchemyBaseGateway, ABC):
    # todo: add filters
    @abstractmethod
    async def get_subscriptions(self) -> List[Subscription]:
        raise NotImplementedError

    @abstractmethod
    async def get_subscription_by_id(
        self,
        subscription_id: int,
    ) -> Subscription:
        raise NotImplementedError
