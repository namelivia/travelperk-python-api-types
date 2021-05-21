from typing import List
from pydantic.dataclasses import dataclass
from .webhook import Webhook


@dataclass
class Webhooks:
    webhooks: List[Webhook]
