from typing import List
from pydantic.dataclasses import dataclass
from .booking import Booking


@dataclass
class Bookings:
    offset: int
    limit: int
    total: int
    bookings: List[Booking]
