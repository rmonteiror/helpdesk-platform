from sqlalchemy.orm import (
    Session,
    joinedload
)

from app.models.comment import Comment


def create_comment(
    db: Session,
    content: str,
    user_id: int,
    ticket_id: int
):
    comment = Comment(
        content=content,
        user_id=user_id,
        ticket_id=ticket_id
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def get_comments_by_ticket(
    db: Session,
    ticket_id: int
):
    return (
        db.query(Comment)
        .options(
            joinedload(Comment.user),
            joinedload(Comment.ticket)
        )
        .filter(
            Comment.ticket_id == ticket_id
        )
        .all()
    )