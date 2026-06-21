from datetime import datetime, timedelta

from app.repositories.ticket_repository import (
    create_ticket,
    get_tickets_by_user,
    get_ticket_by_id,
    update_ticket_status,
    assign_ticket,
    search_tickets
)


def create_new_ticket(
    db,
    title,
    description,
    priority,
    user_id
):
    priority = priority.lower()

    if priority == "high":
        sla_due_date = datetime.utcnow() + timedelta(hours=4)

    elif priority == "medium":
        sla_due_date = datetime.utcnow() + timedelta(hours=24)

    else:
        sla_due_date = datetime.utcnow() + timedelta(hours=72)

    return create_ticket(
        db=db,
        title=title,
        description=description,
        priority=priority,
        user_id=user_id,
        sla_due_date=sla_due_date,
        sla_status="on_time"
    )


def list_user_tickets(
    db,
    user_id,
    skip=0,
    limit=10,
    status=None,
    priority=None,
    sort=None,
    order="asc"
):
    return get_tickets_by_user(
        db,
        user_id,
        skip,
        limit,
        status,
        priority,
        sort,
        order
    )


def search_user_tickets(
    db,
    user_id,
    query_text
):
    return search_tickets(
        db,
        user_id,
        query_text
    )


def find_ticket(
    db,
    ticket_id
):
    return get_ticket_by_id(
        db,
        ticket_id
    )


def change_ticket_status(
    db,
    ticket_id,
    status
):
    ticket = find_ticket(
        db,
        ticket_id
    )

    if not ticket:
        return None

    allowed_status = [
        "open",
        "in_progress",
        "resolved",
        "closed"
    ]

    if status not in allowed_status:
        raise Exception(
            "Invalid status"
        )

    return update_ticket_status(
        db,
        ticket,
        status
    )


def assign_ticket_to_agent(
    db,
    ticket_id,
    agent_id
):
    ticket = find_ticket(
        db,
        ticket_id
    )

    if not ticket:
        return None

    return assign_ticket(
        db,
        ticket,
        agent_id
    )