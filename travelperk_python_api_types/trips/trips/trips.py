from typing import List
from pydantic.dataclasses import dataclass
from .trip import Trip


@dataclass
class Trips:
    offset: int
    limit: int
    total: int
    trips: List[Trip]
