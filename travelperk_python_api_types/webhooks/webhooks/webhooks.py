from typing import List
from dataclasses import dataclass
from .webhook import Webhook


@dataclass
class Webhooks:
    webhooks: List[Webhook]
