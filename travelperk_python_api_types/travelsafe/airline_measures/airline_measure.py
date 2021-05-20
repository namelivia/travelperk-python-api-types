from typing import List
from dataclasses import dataclass
from .airline import Airline
from .info_source import InfoSource
from .safety_measure import SafetyMeasure


@dataclass
class AirlineMeasure:
    airline: Airline
    safety_measures: List[SafetyMeasure]
    info_source: InfoSource
    updated_at: str
