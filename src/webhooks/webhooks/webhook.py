from typing import List
from dataclasses import dataclass


@dataclass
class Webhook:
    id: str
    enabled: bool
    name: str
    url: str
    secret: str
    status: str
    events: List[str]
    successfully_sent: int
    failed_sent: int
    error_rate: float
