from typing import List
from pydantic.dataclasses import dataclass
from .risk_level import RiskLevel
from travelperk_python_api_types.travelsafe.location import Location
from .guideline import Guideline
from travelperk_python_api_types.travelsafe.info_source import InfoSource


@dataclass
class Summary:
    summary: str
    details: str
    risk_level: RiskLevel
    location: Location
    updated_at: str
    guidelines: List[Guideline]
    info_source: InfoSource
