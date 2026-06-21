from app.core.email import (
    send_email
)


def send_ticket_created_email(
    recipient_email: str,
    ticket_title: str
):
    send_email(
        recipient=recipient_email,
        subject="Ticket Created",
        body=f"""
Your ticket has been created successfully.

Title:
{ticket_title}

Our support team will review it shortly.
"""
    )


def send_ticket_assigned_email(
    recipient_email: str,
    ticket_title: str
):
    send_email(
        recipient=recipient_email,
        subject="Ticket Assigned",
        body=f"""
A ticket has been assigned to you.

Title:
{ticket_title}
"""
    )


def send_ticket_resolved_email(
    recipient_email: str,
    ticket_title: str
):
    send_email(
        recipient=recipient_email,
        subject="Ticket Resolved",
        body=f"""
Your ticket has been resolved.

Title:
{ticket_title}

Thank you for using our Help Desk Platform.
"""
    )