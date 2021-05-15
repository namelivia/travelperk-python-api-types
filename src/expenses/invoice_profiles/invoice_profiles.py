from typing import List
from dataclasses import dataclass
from .invoice_profile import InvoiceProfile


@dataclass
class InvoiceProfiles:
    offset: int
    limit: int
    total: int
    profiles: List[InvoiceProfile]
