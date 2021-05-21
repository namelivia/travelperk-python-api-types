from typing import List
from pydantic.dataclasses import dataclass
from .user import User


@dataclass
class Users:
    offset: int
    limit: int
    total: int
    users: List[User]
