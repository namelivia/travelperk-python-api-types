from typing import List
from pydantic.dataclasses import dataclass
from .name import Name
from .emergency_contact import EmergencyContact


@dataclass
class User:
    id: str
    user_name: str
    name: Name
    preferred_language: str
    locale: str
    active: bool
    job_title: str = None
    phone_numbers: List[str]
    emergency_contact: EmergencyContact = None
