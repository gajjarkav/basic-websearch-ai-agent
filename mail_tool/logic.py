# here is the logic and etc config for that tool

import smtplib
from typing import Any

from setting import settings
from mail_tool.schema import SendMailSchema
from email.message import EmailMessage
from langchain_community.tools import tool
import ssl


@tool(args_schema=SendMailSchema)
def send_mail(from_email, password, to_email, subject, body) -> str:
    """
    mail sender tool for sending mail before composing it
    """
    msg = EmailMessage()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.body = body

    try :
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT, context=context) as server:
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Successfully sent email")
    except Exception as e:
        print(f"Failed to send email: {e}")



