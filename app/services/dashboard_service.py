from app.repositories.dashboard_repository import (
    get_ticket_statistics
)


def get_dashboard_stats(
    db
):
    return get_ticket_statistics(
        db
    )