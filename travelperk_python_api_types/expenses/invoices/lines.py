from typing import List
from dataclasses import dataclass


@dataclass
class Lines:
    total: str
    data: List[InvoiceLine]
    next: str
