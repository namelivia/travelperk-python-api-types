from typing import List
from pydantic.dataclasses import dataclass
from .name import Name
from .phone_number import PhoneNumber
from .meta import Meta
from .enterprise_extension import EnterpriseExtension
from .travelperk_extension import TravelperkExtension


@dataclass
class User:
    schemas: List[str]
    name: Name
    locale: str
    preferred_language: str
    id: str
    groups: List[str]
    active: str
    user_name: str
    phone_numbers: List[PhoneNumber]
    meta: Meta
    enterprise_extension: EnterpriseExtension
    travelperk_extension: TravelperkExtension
    title: str = None
    external_id: str = None
