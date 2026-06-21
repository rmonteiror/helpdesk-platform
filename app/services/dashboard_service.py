from app.repositories.dashboard_repository import (
    get_dashboard_metrics
)

from app.services.sla_service import (
    update_sla_status
)


def get_dashboard(
    db
):
    update_sla_status(
        db
    )

    return get_dashboard_metrics(
        db
    )