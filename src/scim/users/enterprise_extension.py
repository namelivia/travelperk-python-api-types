from .manager import Manager
from dataclasses import dataclass


@dataclass
class EnterpriseExtension:
    cost_center: str = None
    manager: Manager
