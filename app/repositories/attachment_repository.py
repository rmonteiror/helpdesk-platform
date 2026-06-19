from sqlalchemy.orm import Session

from app.models.attachment import Attachment


def create_attachment(
    db: Session,
    filename: str,
    file_path: str,
    ticket_id: int
):
    attachment = Attachment(
        filename=filename,
        file_path=file_path,
        ticket_id=ticket_id
    )

    db.add(attachment)
    db.commit()
    db.refresh(attachment)

    return attachment


def get_attachments_by_ticket(
    db: Session,
    ticket_id: int
):
    return (
        db.query(Attachment)
        .filter(
            Attachment.ticket_id == ticket_id
        )
        .all()
    )


def get_attachment_by_id(
    db: Session,
    attachment_id: int
):
    return (
        db.query(Attachment)
        .filter(
            Attachment.id == attachment_id
        )
        .first()
    )


def delete_attachment(
    db: Session,
    attachment: Attachment
):
    db.delete(attachment)
    db.commit()