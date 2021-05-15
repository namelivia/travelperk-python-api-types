from dataclasses import dataclass


@dataclass
class TaxesSummary:
    tax_regime: str = None
    subtotal: str
    tax_percentage: str
    tax_amount: str
    total: str
