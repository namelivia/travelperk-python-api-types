from typing import List
from pydantic.dataclasses import dataclass
from travelperk_python_api_types.expenses.invoice_lines.invoice_line import InvoiceLine


@dataclass
class Lines:
    total: str
    data: List[InvoiceLine]
    next: str
