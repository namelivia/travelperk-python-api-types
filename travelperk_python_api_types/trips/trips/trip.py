from pydantic.dataclasses import dataclass


@dataclass
class Trip:
    id: str
    trip_name: str
    start: str = None
    end: str = None
    status: str
    modified: str
