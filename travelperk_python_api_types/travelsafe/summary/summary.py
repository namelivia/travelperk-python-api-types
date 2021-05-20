from typing import List
from dataclasses import dataclass
from .risk_level import RiskLevel
from .location import Location
from .guideline import Guideline
from .info_source import InfoSource


@dataclass
class Summary:
    serial_number: str
    summary: str
    details: str
    risk_level: RiskLevel
    location: Location
    updated_at: str
    guidelines: List[Guideline]
    info_source: InfoSource
