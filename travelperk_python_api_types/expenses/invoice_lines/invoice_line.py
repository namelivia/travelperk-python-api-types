from pydantic.dataclasses import dataclass
from .metadata import Metadata


@dataclass
class InvoiceLine:
    expense_date: str
    description: str
    quantity: int
    unit_price: str
    non_taxable_unit_price: str
    tax_percentage: str
    tax_amount: str
    tax_regime: str
    total_amount: str
    metadata: Metadata
    invoice_serial_number: str = None
    profile_id: str = None
    profile_name: str = None
    invoice_mode: str = None
    invoice_status: str = None
    issuing_date: str = None
    due_date: str = None
    currency: str = None
