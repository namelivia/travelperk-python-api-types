from typing import List
from dataclasses import dataclass
from .invoice import Invoice


@dataclass
class Invoices:
    offset: int
    limit: int
    total: int
    invoices: List[Invoice]
