from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.ticket import Ticket


def get_ticket_statistics(
    db: Session
):
    total = db.query(
        func.count(Ticket.id)
    ).scalar()

    open_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.status == "open"
    ).scalar()

    in_progress_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.status == "in_progress"
    ).scalar()

    resolved_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.status == "resolved"
    ).scalar()

    closed_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.status == "closed"
    ).scalar()

    high_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.priority == "high"
    ).scalar()

    medium_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.priority == "medium"
    ).scalar()

    low_count = db.query(
        func.count(Ticket.id)
    ).filter(
        Ticket.priority == "low"
    ).scalar()

    return {
        "total_tickets": total,
        "open": open_count,
        "in_progress": in_progress_count,
        "resolved": resolved_count,
        "closed": closed_count,
        "high": high_count,
        "medium": medium_count,
        "low": low_count
    }