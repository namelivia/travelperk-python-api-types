from typing import List
from pydantic.dataclasses import dataclass
from .invoice_profile import InvoiceProfile
from .emergency_contact import EmergencyContact


@dataclass
class TravelperkExtension:
    gender: str = None
    date_of_birth: str = None
    travel_policy: str = None
    invoice_profiles: List[InvoiceProfile]
    emergency_contact: EmergencyContact
