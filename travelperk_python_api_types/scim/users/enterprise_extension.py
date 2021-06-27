from .manager import Manager
from pydantic.dataclasses import dataclass


@dataclass
class EnterpriseExtension:
    cost_center: str = None
    manager: Manager = None
    country_or_residence: str = None
