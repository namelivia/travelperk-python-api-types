from typing import List
from dataclasses import dataclass
from .user import User
from .vendor import Vendor


@dataclass
class Metadata:
    trip_id: int = None
    trip_name: str = None
    service: str
    travelers: List[User]
    start_date: str = None
    end_date: str = None
    cost_center: str = None
    labels: List[str] = None
    vendor: Vendor = None
    out_of_policy: bool = None
    approvers: List[User]
    booker: User = None
