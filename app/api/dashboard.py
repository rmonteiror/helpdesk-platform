from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.api.users import get_current_user

from app.schemas.dashboard_response import (
    DashboardResponse
)

from app.services.dashboard_service import (
    get_dashboard
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/",
    response_model=DashboardResponse
)
def dashboard(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_dashboard(
        db
    )