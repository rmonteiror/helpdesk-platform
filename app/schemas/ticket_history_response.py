from pydantic import BaseModel
from datetime import datetime


class TicketHistoryResponse(BaseModel):
    id: int
    ticket_id: int
    performed_by: int
    action: str
    created_at: datetime

    class Config:
        from_attributes = True