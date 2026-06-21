from fastapi import FastAPI

from app.database.connection import engine
from app.database.base import Base

from app.models.user import User
from app.models.ticket import Ticket
from app.models.comment import Comment
from app.models.attachment import Attachment
from app.models.ticket_history import TicketHistory

from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.tickets import router as tickets_router
from app.api.comments import router as comments_router

from app.api.dashboard import (
    router as dashboard_router
)
from app.api.attachments import (
    router as attachments_router
)

from app.api.ticket_history import (
    router as history_router
)
from app.api.dashboard import router as dashboard_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Help Desk Management API",
    version="1.0.0",
    description="REST API for ticket management, authentication and user administration."
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(tickets_router)
app.include_router(comments_router)
app.include_router(
    dashboard_router
)
app.include_router(
    attachments_router
)
app.include_router(
    history_router
)
app.include_router(
    dashboard_router
)


@app.get("/")
def root():
    return {
        "message": "Help Desk Platform API Running"
    }
@app.get("/healthz")
def health_check():
    return {
        "status": "healthy"
    }