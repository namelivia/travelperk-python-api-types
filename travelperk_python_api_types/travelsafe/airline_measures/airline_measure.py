from typing import List
from pydantic.dataclasses import dataclass
from .airline import Airline
from travelperk_python_api_types.travelsafe.info_source import InfoSource
from .safety_measure import SafetyMeasure


@dataclass
class AirlineMeasure:
    airline: Airline
    safety_measures: List[SafetyMeasure]
    info_source: InfoSource
    updated_at: str
