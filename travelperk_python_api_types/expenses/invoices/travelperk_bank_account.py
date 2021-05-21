from pydantic.dataclasses import dataclass


@dataclass
class TravelperkBankAccount:
    bank_name: str
    account_number: str
    bic: str
    reference: str
