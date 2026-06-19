from pydantic import BaseModel
from datetime import datetime


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    user_id: int
    assigned_to: int | None
    created_at: datetime

    class Config:
        from_attributes = True
