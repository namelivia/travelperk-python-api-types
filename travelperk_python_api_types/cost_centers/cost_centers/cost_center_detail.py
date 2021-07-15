from typing import List
from pydantic.dataclasses import dataclass
from .user import User


@dataclass
class CostCenterDetail:
    id: int
    name: str
    archived: bool
    users: List[User]
    count_users: int
