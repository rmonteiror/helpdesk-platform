from app.models.ticket import Ticket


def get_ticket_stats(db):
    total_tickets = db.query(Ticket).count()

    open_tickets = db.query(Ticket).filter(
        Ticket.status == "open"
    ).count()

    in_progress_tickets = db.query(Ticket).filter(
        Ticket.status == "in_progress"
    ).count()

    resolved_tickets = db.query(Ticket).filter(
        Ticket.status == "resolved"
    ).count()

    closed_tickets = db.query(Ticket).filter(
        Ticket.status == "closed"
    ).count()

    return {
        "total_tickets": total_tickets,
        "open": open_tickets,
        "in_progress": in_progress_tickets,
        "resolved": resolved_tickets,
        "closed": closed_tickets
    }