from fastapi import HTTPException


def require_agent_or_admin(user):
    if user.role not in [
        "agent",
        "admin"
    ]:
        raise HTTPException(
            status_code=403,
            detail="Permission denied"
        )


def require_admin(user):
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin only"
        )