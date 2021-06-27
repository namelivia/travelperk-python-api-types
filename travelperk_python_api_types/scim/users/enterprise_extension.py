from .manager import Manager
from pydantic.dataclasses import dataclass


@dataclass
class EnterpriseExtension:
    country_or_residence: str
    cost_center: str = None
    manager: Manager = None
