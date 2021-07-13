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
    successfully_sent: int = None
    failed_sent: int = None
    error_rate: float = None
