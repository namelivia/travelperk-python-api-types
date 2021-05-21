from typing import List
from pydantic.dataclasses import dataclass


@dataclass
class Lines:
    total: str
    data: List[InvoiceLine]
    next: str
