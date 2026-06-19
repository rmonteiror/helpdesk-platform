from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.ticket import (
    TicketCreate
)

from app.schemas.ticket_status import (
    TicketStatusUpdate
)

from app.schemas.ticket_assignment import (
    TicketAssignment
)

from app.schemas.ticket_response import (
    TicketResponse
)

from app.api.users import get_current_user

from app.core.permissions import (
    require_agent_or_admin
)

from app.services.ticket_service import (
    create_new_ticket,
    list_user_tickets,
    search_user_tickets,
    find_ticket,
    change_ticket_status,
    assign_ticket_to_agent
)

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post(
    "/",
    response_model=TicketResponse
)
def create_ticket(
    ticket: TicketCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_new_ticket(
        db=db,
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        user_id=current_user.id
    )


@router.get(
    "/",
    response_model=list[TicketResponse]
)
def my_tickets(
    skip: int = 0,
    limit: int = 10,
    status: str | None = None,
    priority: str | None = None,
    sort: str | None = None,
    order: str = "asc",
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return list_user_tickets(
        db,
        current_user.id,
        skip,
        limit,
        status,
        priority,
        sort,
        order
    )


@router.get(
    "/search",
    response_model=list[TicketResponse]
)
def search_tickets(
    q: str,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return search_user_tickets(
        db,
        current_user.id,
        q
    )


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket(
    ticket_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    ticket = find_ticket(
        db,
        ticket_id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.patch("/{ticket_id}/status")
def update_status(
    ticket_id: int,
    payload: TicketStatusUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    require_agent_or_admin(
        current_user
    )

    ticket = change_ticket_status(
        db,
        ticket_id,
        payload.status
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "id": ticket.id,
        "status": ticket.status
    }


@router.patch("/{ticket_id}/assign")
def assign_ticket(
    ticket_id: int,
    payload: TicketAssignment,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    require_agent_or_admin(
        current_user
    )

    ticket = assign_ticket_to_agent(
        db,
        ticket_id,
        payload.agent_id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "id": ticket.id,
        "assigned_to": ticket.assigned_to
    }