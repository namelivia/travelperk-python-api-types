from pydantic.dataclasses import dataclass
from travelperk_python_api_types.trips.location import Location


@dataclass
class Destination:
    location: Location
    time: str
