from pydantic.dataclasses import dataclass
from .location import Location


@dataclass
class Origin:
    location: Location
    time: str
