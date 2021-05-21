from typing import List
from pydantic.dataclasses import dataclass
from .segment import Segment


@dataclass
class Leg:
    segments: List[Segment]
