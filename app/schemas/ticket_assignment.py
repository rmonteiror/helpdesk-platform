from pydantic import BaseModel


class TicketAssignment(BaseModel):
    agent_id: int