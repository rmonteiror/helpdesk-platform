from pydantic import BaseModel
from datetime import datetime


class CommentUser(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CommentTicket(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime

    user: CommentUser
    ticket: CommentTicket

    class Config:
        from_attributes = True