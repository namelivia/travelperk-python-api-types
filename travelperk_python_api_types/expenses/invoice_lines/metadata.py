from typing import List
from pydantic.dataclasses import dataclass
from .user import User
from .vendor import Vendor


@dataclass
class Metadata:
    service: str
    travelers: List[User]
    approvers: List[User]
    trip_id: int = None
    trip_name: str = None
    start_date: str = None
    end_date: str = None
    cost_center: str = None
    labels: List[str] = None
    vendor: Vendor = None
    out_of_policy: bool = None
    booker: User = None
