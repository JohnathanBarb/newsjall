from sqlalchemy.orm import Mapped, mapped_column

from src.shared.models import Base, CreatedAtUpdatedAtMixin, UUIDMixin


class User(Base, UUIDMixin, CreatedAtUpdatedAtMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str]
    hash_password: Mapped[str]
