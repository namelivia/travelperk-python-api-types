from pydantic.dataclasses import dataclass


@dataclass
class TravelDocument:
    document_type: str
    document_number: str
    given_name: str
    middle_name: str
    family_name: str
    gender: str
    issuing_country: str
    issuing_date: str
    expiration_date: str
    citizenship: str
