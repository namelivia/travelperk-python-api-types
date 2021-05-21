from pydantic.dataclasses import dataclass


@dataclass
class BillingInformation:
    legal_name: str
    vat_number: str
    address_line_1: str
    address_line_2: str
    city: str
    postal_code: str
    country_name: str
