from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    status = Column(
        String,
        default="open"
    )

    priority = Column(
        String,
        default="medium"
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        foreign_keys=[user_id],
        back_populates="tickets"
    )

    comments = relationship(
        "Comment",
        back_populates="ticket",
        cascade="all, delete-orphan"
    )

    attachments = relationship(
        "Attachment",
        cascade="all, delete-orphan"
    )