import requests
from pydantic import BaseModel
from secret_santa.email import Email


class MailGunSender(BaseModel):
    """Send emails via mailgun"""
    api_key: str
    email_domain: str
    sender_name: str
    sender_email: str

    def send_email(self, email: Email) -> None:
        requests.post(
            f"https://api.mailgun.net/v3/{self.email_domain}/messages",
            auth=("api", self.api_key),
            data={
                "from": f"{self.sender_name} <{self.sender_email}>",
                "to": [email.recipient_email],
                "subject": email.subject,
                "text": email.body
            },
            timeout=5 * 60,
        )
