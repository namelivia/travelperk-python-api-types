from typing import List
from pydantic.dataclasses import dataclass
from .invoice_profile import InvoiceProfile


@dataclass
class InvoiceProfiles:
    offset: int
    limit: int
    total: int
    profiles: List[InvoiceProfile]
