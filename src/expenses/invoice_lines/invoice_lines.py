from typing import List
from dataclasses import dataclass
from .invoice_line import InvoiceLine


@dataclass
class InvoiceLines:
    offset: int
    limit: int
    total: int
    invoice_lines: List[InvoiceLine]
