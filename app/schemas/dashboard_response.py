from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_tickets: int
    open_tickets: int
    in_progress_tickets: int
    resolved_tickets: int
    closed_tickets: int
    overdue_sla: int