from typing import List
from pydantic.dataclasses import dataclass
from .location import Location
from .reference import Reference
from .leg import Leg


@dataclass
class Booking:
    id: str
    start: str
    end: str
    type: str
    status: str
    modified: str
    trip_id: str
    references: List[Reference]
    location: Location = None
    legs: List[Leg] = None
