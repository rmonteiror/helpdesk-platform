from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.ticket import Ticket


def get_dashboard_metrics(
    db: Session
):
    total = db.query(Ticket).count()

    open_count = (
        db.query(Ticket)
        .filter(Ticket.status == "open")
        .count()
    )

    in_progress_count = (
        db.query(Ticket)
        .filter(Ticket.status == "in_progress")
        .count()
    )

    resolved_count = (
        db.query(Ticket)
        .filter(Ticket.status == "resolved")
        .count()
    )

    closed_count = (
        db.query(Ticket)
        .filter(Ticket.status == "closed")
        .count()
    )

    overdue_count = (
        db.query(Ticket)
        .filter(Ticket.sla_status == "overdue")
        .count()
    )

    return {
        "total_tickets": total,
        "open_tickets": open_count,
        "in_progress_tickets": in_progress_count,
        "resolved_tickets": resolved_count,
        "closed_tickets": closed_count,
        "overdue_sla": overdue_count
    }