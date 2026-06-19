from sqlalchemy.orm import Session

from app.models.ticket_history import (
    TicketHistory
)


def create_history(
    db: Session,
    ticket_id: int,
    performed_by: int,
    action: str
):
    history = TicketHistory(
        ticket_id=ticket_id,
        performed_by=performed_by,
        action=action
    )

    db.add(history)
    db.commit()
    db.refresh(history)

    return history


def get_ticket_history(
    db: Session,
    ticket_id: int
):
    return (
        db.query(TicketHistory)
        .filter(
            TicketHistory.ticket_id == ticket_id
        )
        .order_by(
            TicketHistory.created_at.desc()
        )
        .all()
    )