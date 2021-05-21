from typing import List
from pydantic.dataclasses import dataclass


@dataclass
class CostCenterDetail:
    id: str
    name: str
    archived: bool
    # TODO: Import User once its done
    # users: List[User]
    const_users: int
