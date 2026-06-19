from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.api.users import (
    get_current_user
)

from app.services.ticket_history_service import (
    list_history
)

from app.schemas.ticket_history_response import (
    TicketHistoryResponse
)

router = APIRouter(
    prefix="/history",
    tags=["Ticket History"]
)


@router.get(
    "/{ticket_id}",
    response_model=list[TicketHistoryResponse]
)
def get_history(
    ticket_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return list_history(
        db,
        ticket_id
    )