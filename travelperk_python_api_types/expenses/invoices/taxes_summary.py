from pydantic.dataclasses import dataclass


@dataclass
class TaxesSummary:
    subtotal: str
    tax_percentage: str
    tax_amount: str
    total: str
    tax_regime: str = None
