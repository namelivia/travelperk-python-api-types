from pydantic.dataclasses import dataclass
from travelperk_python_api_types.trips.location import Location


@dataclass
class Origin:
    location: Location
    time: str
