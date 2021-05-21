from typing import List
from pydantic.dataclasses import dataclass
from .location import Location
from .requirement import Requirement
from .info_source import InfoSource


@dataclass
class Restriction:
    serial_number: str
    origin: Location
    destination: Location
    authorization_status: str
    summary: str
    details: str
    start_date: str
    end_date: str
    updated_at: str
    requirements: List[Requirement]
    info_source: InfoSource
