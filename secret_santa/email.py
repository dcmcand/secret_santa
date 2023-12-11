from typing import Protocol

from pydantic import BaseModel


class Email(BaseModel):
    recipient_email: str
    subject: str = "Secret Santa"
    body: str


class MailSender(Protocol):
    """An interface to allow sending emails"""
    def send_email(self, email: Email) -> None:
        ...


def generate_email_body(
        gifter_name: str, giftee_name: str, giftee_interests: list[str]
        ) -> str:
    """Generates the text for an email body"""
    return f"Hi {gifter_name},\nThis is your secret santa assignment! \n" \
           f"This Christmas, you will buy a gift for {giftee_name}.\n" \
           f"{generate_interests_message(giftee_interests)}Remember this is" \
           " a SECRET Santa so ssssshhhhhhh!\nMerry Christmas\nSanta Claus"


def email_assignment(
        gifter_email: str, gifter_name: str, giftee_name: str,
        giftee_interests: list[str], email_sender: MailSender,) -> None:
    """Send a simple message to a specific email address"""
    email_sender.send_email(
       Email(
           recipient_email=gifter_email,
           body=generate_email_body(
               gifter_name=gifter_name, giftee_name=giftee_name,
               giftee_interests=giftee_interests)
       )
    )


def generate_interests_message(interests: list[str]) -> str:
    """Returns a string of the interests of a giftee"""
    if len(interests) <= 0:
        return ""
    msg = "They wrote to Santa and said they were interested in "
    for interest in interests[:-1]:
        msg += f"{interest},"
    if len(interests) > 1:
        msg += " and "
    msg += f"{interests[-1]}.\n"
    return msg
