from pydantic.dataclasses import dataclass
from .location import Location


@dataclass
class Destination:
    location: Location
    time: str
