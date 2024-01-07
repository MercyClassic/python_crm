from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.database import Base


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    price: Mapped[Decimal]
