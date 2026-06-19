from app.repositories.attachment_repository import (
    create_attachment,
    get_attachments_by_ticket,
    get_attachment_by_id,
    delete_attachment
)


def add_attachment(
    db,
    filename,
    file_path,
    ticket_id
):
    return create_attachment(
        db=db,
        filename=filename,
        file_path=file_path,
        ticket_id=ticket_id
    )


def list_attachments(
    db,
    ticket_id
):
    return get_attachments_by_ticket(
        db,
        ticket_id
    )


def remove_attachment(
    db,
    attachment_id
):
    attachment = get_attachment_by_id(
        db,
        attachment_id
    )

    if not attachment:
        return False

    delete_attachment(
        db,
        attachment
    )

    return True