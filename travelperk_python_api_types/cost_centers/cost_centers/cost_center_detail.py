from typing import List
from pydantic.dataclasses import dataclass
from .user import User


@dataclass
class CostCenterDetail:
    id: str
    name: str
    archived: bool
    users: List[User]
    count_users: int
