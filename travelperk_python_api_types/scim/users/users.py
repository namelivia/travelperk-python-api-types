from typing import List
from pydantic.dataclasses import dataclass
from .user import User


@dataclass
class Users:
    schemas: List[str]
    total_results: int
    items_per_page: int
    start_index: int
    resources: List[User]
