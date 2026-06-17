from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    user_id: int

    class Config:
        from_attributes = True