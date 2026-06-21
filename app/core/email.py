import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = os.getenv(
    "SMTP_SERVER",
    "smtp.gmail.com"
)

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        587
    )
)

SMTP_USERNAME = os.getenv(
    "SMTP_USERNAME",
    ""
)

SMTP_PASSWORD = os.getenv(
    "SMTP_PASSWORD",
    ""
)


def send_email(
    recipient: str,
    subject: str,
    body: str
):
    message = MIMEMultipart()

    message["From"] = SMTP_USERNAME
    message["To"] = recipient
    message["Subject"] = subject

    message.attach(
        MIMEText(
            body,
            "plain"
        )
    )

    with smtplib.SMTP(
        SMTP_SERVER,
        SMTP_PORT
    ) as server:

        server.starttls()

        server.login(
            SMTP_USERNAME,
            SMTP_PASSWORD
        )

        server.send_message(
            message
        )