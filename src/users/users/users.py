from typing import List
from dataclasses import dataclass
from .user import User


@dataclass
class Users:
    offset: int
    limit: int
    total: int
    users: List[User]
