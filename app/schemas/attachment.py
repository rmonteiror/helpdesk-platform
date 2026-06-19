from pydantic import BaseModel


class AttachmentCreate(BaseModel):
    filename: str
    file_path: str