from pydantic.dataclasses import dataclass
from travelperk_python_api_types.trips.location import Location


@dataclass
class Trip:
    id: str
    booker_id: str
    trip_name: str
    status: str
    modified: str
    start: str = None
    start_datetime_utc: str = None
    end_datetime_utc: str = None
    start_datetime_local: str = None
    end_datetime_local: str = None
    start_location: Location = None
    end_location: Location = None
    end: str = None
