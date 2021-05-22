from typing import List
from pydantic.dataclasses import dataclass
from travelperk_python_api_types.users.users.user import User


@dataclass
class CostCenterDetail:
    id: str
    name: str
    archived: bool
    users: List[User]
    const_users: int
