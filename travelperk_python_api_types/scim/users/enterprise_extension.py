from .manager import Manager
from pydantic.dataclasses import dataclass


@dataclass
class EnterpriseExtension:
    manager: Manager
    cost_center: str = None
