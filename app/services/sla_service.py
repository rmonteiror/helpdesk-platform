from datetime import datetime

from app.models.ticket import Ticket


def update_sla_status(
    db
):
    tickets = (
        db.query(Ticket)
        .filter(
            Ticket.status.notin_(
                ["resolved", "closed"]
            )
        )
        .all()
    )

    updated = 0

    for ticket in tickets:

        if (
            ticket.sla_due_date
            and datetime.utcnow() > ticket.sla_due_date
            and ticket.sla_status != "overdue"
        ):
            ticket.sla_status = "overdue"
            updated += 1

    db.commit()

    return updated