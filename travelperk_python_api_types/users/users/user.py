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
    phone_numbers: List[str]
    job_title: str = None
    emergency_contact: EmergencyContact = None
