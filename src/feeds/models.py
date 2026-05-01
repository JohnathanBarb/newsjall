import uuid
from datetime import datetime

from sqlalchemy import UUID, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.shared.models import Base, CreatedAtUpdatedAtMixin, UUIDMixin


class Feed(Base, CreatedAtUpdatedAtMixin, UUIDMixin):
    __tablename__ = "feeds"

    title: Mapped[str]
    url: Mapped[str] = mapped_column(String(2048), unique=True, index=True)
    description: Mapped[str | None] = mapped_column(Text)

    last_fetched_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class Post(Base, CreatedAtUpdatedAtMixin, UUIDMixin):
    __tablename__ = "posts"

    external_id: Mapped[str] = mapped_column(String(512))

    feed_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("feeds.id", ondelete="CASCADE"),
        index=True,
    )
    title: Mapped[str]
    link: Mapped[str] = mapped_column(String(2048))
    content: Mapped[str | None] = mapped_column(Text)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class Subscription(Base, CreatedAtUpdatedAtMixin, UUIDMixin):
    __tablename__ = "subscriptions"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    feed_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("feeds.id", ondelete="CASCADE"),
        primary_key=True,
    )
