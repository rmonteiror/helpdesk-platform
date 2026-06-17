from app.repositories.comment_repository import (
    create_comment,
    get_comments_by_ticket
)


def add_comment(
    db,
    content,
    user_id,
    ticket_id
):
    return create_comment(
        db=db,
        content=content,
        user_id=user_id,
        ticket_id=ticket_id
    )


def list_comments(
    db,
    ticket_id
):
    return get_comments_by_ticket(
        db,
        ticket_id
    )