from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.api.users import get_current_user

from app.core.permissions import (
    require_agent_or_admin
)

from app.services.dashboard_service import (
    get_dashboard_stats
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    require_agent_or_admin(
        current_user
    )

    return get_dashboard_stats(
        db
    )