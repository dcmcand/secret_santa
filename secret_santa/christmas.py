"""Secret Santa"""
from typing import Optional
import random
from pydantic import BaseModel
from secret_santa.email import MailSender
from secret_santa.parser import Participant, parse_csv
from secret_santa.email import email_assignment


class Gifter(BaseModel):
    """The person giving gifts for secret santa"""
    name: str
    email: str
    significant_other: Optional[str]


class Giftee(BaseModel):
    """The person recieving the gifts from secret santa"""
    name: str
    interests: list[str]


class Assignment(BaseModel):
    """A pairing of a giftee and a gifter"""
    gifter: Gifter
    giftee: Giftee


def split_participant_list(participants: list[Participant]) -> tuple[list[Gifter], list[Giftee]]:
    """Generates a list of Giftees and Gifters from a list of Participants"""
    gifters = []
    giftees = []
    for participant in participants:
        gifters.append(Gifter(
            name=participant.name,
            email=participant.email,
            significant_other=participant.significant_other
            )
        )
        giftees.append(
            Giftee(
                name=participant.name,
                interests=participant.interests
            )
        )
    return (gifters, giftees)


def assign_names(participants: list[Participant]) -> list[Assignment]:
    """Assign pairs of giftees and gifters and returns a list of assignments"""
    gifters, giftees = split_participant_list(participants)
    assignments = []
    try:
        for gifter in gifters:
            giftee = get_giftee(gifter, giftees)
            del giftees[giftees.index(giftee)]
            assignments.append(Assignment(gifter=gifter, giftee=giftee))
    except SystemError as err:
        raise SystemError(err)
    except Exception:
        return assign_names(participants)
    return assignments
    

def get_giftee(gifter: Gifter, giftee_list: list[Giftee]) -> Giftee:
    """
    Select a random name from a list of names
    Will not return the gifters name or
    the gifter's significant other
    """
    potential_choices = [
        giftee for giftee in giftee_list if giftee.name != gifter.name and giftee.name != gifter.significant_other
        ]
    if len(potential_choices) < 1:
        raise SystemError(f"no giftees available for {gifter.name} in list {[x.name for x in giftee_list]}")
    return random.choice(potential_choices)


def send_secret_santa(
        mailer: MailSender, participants: list[Participant]
        ) -> list[tuple[str, str]]:
    assignments = assign_names(participants)
    pairs = []
    for assignment in assignments:
        pairs.append((assignment.gifter.name, assignment.giftee.name))
        email_assignment(
            gifter_email=assignment.gifter.email,
            gifter_name=assignment.gifter.name,
            giftee_name=assignment.giftee.name,
            giftee_interests=assignment.giftee.interests,
            email_sender=mailer
        )
    return pairs

