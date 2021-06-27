from .manager import Manager
from pydantic.dataclasses import dataclass


@dataclass
class EnterpriseExtension:
    cost_center: str = None
    manager: Manager = None
