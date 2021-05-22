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
    invoice_serial_number: str
    profile_id: str
    profile_name: str
    invoice_mode: str
    invoice_status: str
    issuing_date: str
    due_date: str
    currency: str
