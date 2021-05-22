from typing import List
from pydantic.dataclasses import dataclass
from travelperk_python_api_types.expenses.billing_information import BillingInformation
from .lines import Lines
from .taxes_summary import TaxesSummary
from .travelperk_bank_account import TravelperkBankAccount


@dataclass
class Invoice:
    serial_number: str
    profile_id: str
    profile_name: str
    billing_information: BillingInformation
    mode: str
    status: str
    issuing_date: str
    billing_period: str
    from_date: str
    to_date: str
    due_date: str
    currency: str
    total: str
    lines: Lines
    taxes_summary: List[TaxesSummary]
    reference: str
    pdf: str
    travelperk_bank_account: TravelperkBankAccount = None
