from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session

from pydantic import BaseModel

from app.database.connection import get_db

from app.core.security import decode_access_token

from app.core.permissions import (
    require_admin
)

from app.repositories.user_repository import (
    get_user_by_email
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

security = HTTPBearer()


class RoleUpdate(BaseModel):
    role: str


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    email = payload.get("sub")

    user = get_user_by_email(
        db,
        email
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    }


@router.patch("/{user_id}/role")
def update_user_role(
    user_id: int,
    payload: RoleUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    require_admin(
        current_user
    )

    from app.models.user import User

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    allowed_roles = [
        "user",
        "agent",
        "admin"
    ]

    if payload.role not in allowed_roles:
        raise HTTPException(
            status_code=400,
            detail="Invalid role"
        )

    user.role = payload.role

    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }