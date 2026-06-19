from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.api.users import get_current_user

from app.schemas.comment import (
    CommentCreate
)

from app.schemas.comment_response import (
    CommentResponse
)

from app.services.comment_service import (
    add_comment,
    list_comments
)

router = APIRouter(
    prefix="/tickets",
    tags=["Comments"]
)


@router.post(
    "/{ticket_id}/comments",
    response_model=CommentResponse
)
def create_comment(
    ticket_id: int,
    payload: CommentCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return add_comment(
        db=db,
        content=payload.content,
        user_id=current_user.id,
        ticket_id=ticket_id
    )


@router.get(
    "/{ticket_id}/comments",
    response_model=list[CommentResponse]
)
def get_comments(
    ticket_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return list_comments(
        db,
        ticket_id
    )