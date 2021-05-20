from typing import List
from dataclasses import dataclass
from .segment import Segment


@dataclass
class Leg:
    segments: List[Segment]
