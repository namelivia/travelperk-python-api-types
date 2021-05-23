from pydantic.dataclasses import dataclass
from travelperk_python_api_types.expenses.billing_information import BillingInformation


@dataclass
class InvoiceProfile:
    id: str
    name: str
    payment_method_type: str
    billing_period: str
    currency: str
    billing_information: BillingInformation
