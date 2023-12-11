"""Parse a CSV and turn it into a list of participants"""
from typing import Optional
import csv
from pydantic import BaseModel


class Participant(BaseModel):
    """A participant in secret santa"""
    name: str
    email: str
    interests: list[str]
    significant_other: Optional[str]


def parse_csv(path: str) -> list[Participant]:
    """Parses a CSV and returns secret santa participants"""
    participants = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True, )
        # Skip the header row
        next(reader, None)
        for row in reader:
            name, email, significant_other, interests = row
            participants.append(
                Participant(
                    name=name,
                    email=email,
                    significant_other=significant_other,
                    # Break interests into list and strip extra whitespace
                    interests=[x.strip() for x in interests.split(",")],
                )
            )
    return participants
