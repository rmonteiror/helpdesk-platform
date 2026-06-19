from pydantic import BaseModel
from datetime import datetime


class AttachmentResponse(BaseModel):
    id: int
    filename: str
    file_path: str
    uploaded_at: datetime
    ticket_id: int

    class Config:
        from_attributes = True