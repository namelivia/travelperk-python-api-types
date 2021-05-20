from typing import List
from dataclasses import dataclass
from .trip import Trip


@dataclass
class Trips:
    offset: int
    limit: int
    total: int
    trips: List[Trip]
