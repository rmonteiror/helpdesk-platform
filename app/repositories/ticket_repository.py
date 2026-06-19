from sqlalchemy.orm import Session
from sqlalchemy import desc, or_

from app.models.ticket import Ticket


def create_ticket(
    db: Session,
    title: str,
    description: str,
    priority: str,
    user_id: int
):
    ticket = Ticket(
        title=title,
        description=description,
        priority=priority,
        user_id=user_id
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_tickets_by_user(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    status: str = None,
    priority: str = None,
    sort: str = None,
    order: str = "asc"
):
    query = db.query(Ticket).filter(
        Ticket.user_id == user_id
    )

    if status:
        query = query.filter(
            Ticket.status == status
        )

    if priority:
        query = query.filter(
            Ticket.priority == priority
        )

    if sort == "created_at":

        if order == "desc":
            query = query.order_by(
                desc(Ticket.created_at)
            )
        else:
            query = query.order_by(
                Ticket.created_at
            )

    elif sort == "priority":

        if order == "desc":
            query = query.order_by(
                desc(Ticket.priority)
            )
        else:
            query = query.order_by(
                Ticket.priority
            )

    elif sort == "status":

        if order == "desc":
            query = query.order_by(
                desc(Ticket.status)
            )
        else:
            query = query.order_by(
                Ticket.status
            )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def search_tickets(
    db: Session,
    user_id: int,
    query_text: str
):
    return (
        db.query(Ticket)
        .filter(
            Ticket.user_id == user_id
        )
        .filter(
            or_(
                Ticket.title.ilike(
                    f"%{query_text}%"
                ),
                Ticket.description.ilike(
                    f"%{query_text}%"
                )
            )
        )
        .all()
    )


def get_ticket_by_id(
    db: Session,
    ticket_id: int
):
    return db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()


def update_ticket_status(
    db,
    ticket,
    status
):
    ticket.status = status

    db.commit()
    db.refresh(ticket)

    return ticket


def assign_ticket(
    db,
    ticket,
    agent_id
):
    ticket.assigned_to = agent_id

    db.commit()
    db.refresh(ticket)

    return ticket