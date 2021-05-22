from pydantic.dataclasses import dataclass


@dataclass
class Trip:
    id: str
    trip_name: str
    status: str
    modified: str
    start: str = None
    end: str = None
