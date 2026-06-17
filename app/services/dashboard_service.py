from app.repositories.dashboard_repository import (
    get_ticket_stats
)


def get_dashboard_stats(db):
    return get_ticket_stats(db)