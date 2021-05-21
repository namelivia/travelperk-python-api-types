from typing import List
from pydantic.dataclasses import dataclass
from .invoice import Invoice


@dataclass
class Invoices:
    offset: int
    limit: int
    total: int
    invoices: List[Invoice]
