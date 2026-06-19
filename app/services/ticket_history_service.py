from app.repositories.ticket_history_repository import (
    create_history,
    get_ticket_history
)


def add_history(
    db,
    ticket_id,
    performed_by,
    action
):
    return create_history(
        db=db,
        ticket_id=ticket_id,
        performed_by=performed_by,
        action=action
    )


def list_history(
    db,
    ticket_id
):
    return get_ticket_history(
        db,
        ticket_id
    )