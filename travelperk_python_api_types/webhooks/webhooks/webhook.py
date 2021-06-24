from typing import List
from pydantic.dataclasses import dataclass


@dataclass
class Webhook:
    id: str
    name: str
    url: str
    secret: str
    enabled: bool
    events: List[str]
    successfully_sent: int
    failed_sent: int
    error_rate: float
