from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.api.users import get_current_user

from app.repositories.attachment_repository import (
    get_attachment_by_id
)

from app.services.attachment_service import (
    add_attachment,
    list_attachments,
    remove_attachment
)

from app.services.ticket_history_service import (
    add_history
)

from app.core.file_manager import (
    save_file
)

router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"]
)


@router.post("/upload/{ticket_id}")
def upload_attachment(
    ticket_id: int,
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    file_path = save_file(
        file,
        file.filename
    )

    attachment = add_attachment(
        db=db,
        filename=file.filename,
        file_path=file_path,
        ticket_id=ticket_id
    )

    add_history(
        db=db,
        ticket_id=ticket_id,
        performed_by=current_user.id,
        action=f"Attachment uploaded: {file.filename}"
    )

    return attachment


@router.get("/tickets/{ticket_id}")
def get_attachments(
    ticket_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return list_attachments(
        db,
        ticket_id
    )


@router.delete("/{attachment_id}")
def delete_attachment_endpoint(
    attachment_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    attachment = get_attachment_by_id(
        db,
        attachment_id
    )

    if not attachment:
        raise HTTPException(
            status_code=404,
            detail="Attachment not found"
        )

    ticket_id = attachment.ticket_id
    filename = attachment.filename

    success = remove_attachment(
        db,
        attachment_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Attachment not found"
        )

    add_history(
        db=db,
        ticket_id=ticket_id,
        performed_by=current_user.id,
        action=f"Attachment deleted: {filename}"
    )

    return {
        "message": "Attachment deleted successfully"
    }


@router.get("/download/{attachment_id}")
def download_attachment(
    attachment_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    attachment = get_attachment_by_id(
        db,
        attachment_id
    )

    if not attachment:
        raise HTTPException(
            status_code=404,
            detail="Attachment not found"
        )

    return FileResponse(
        path=attachment.file_path,
        filename=attachment.filename
    )