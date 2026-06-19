from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        default="user"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    tickets = relationship(
        "Ticket",
        foreign_keys="Ticket.user_id",
        back_populates="user"
    )

    comments = relationship(
        "Comment",
        back_populates="user"
    )