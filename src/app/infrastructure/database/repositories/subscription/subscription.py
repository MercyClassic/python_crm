from typing import List

from sqlalchemy import select

from app.domain.models.subscription.subscription import Subscription
from app.infrastructure.database.interfaces.repositories.subscription.subscription import (
    SubscriptionRepositoryInterface,
)
from app.infrastructure.database.models.subscription.subscription import (
    Subscription as SubscriptionDB,
)


class SubscriptionRepository(SubscriptionRepositoryInterface):
    # todo: add filters
    async def get_subscriptions(self) -> List[Subscription]:
        query = select(SubscriptionDB)
        result = (await self._session.execute(query)).scalars().all()
        return result

    async def get_subscription_by_id(
        self,
        subscription_id: int,
    ) -> Subscription:
        query = select(SubscriptionDB).where(subscription_id=subscription_id)
        result = (await self._session.execute(query)).scalar()
        return result
