from typing import List, Optional
from pydantic.dataclasses import dataclass
from travelperk_python_api_types.travelsafe.location import Location
from .requirement import Requirement
from travelperk_python_api_types.travelsafe.info_source import InfoSource


@dataclass
class Restriction:
    origin: Location
    destination: Location
    authorization_status: str
    summary: str
    details: str
    start_date: str
    end_date: Optional[str]
    updated_at: str
    requirements: List[Requirement]
    info_source: InfoSource
