from typing import List
from pydantic.dataclasses import dataclass
from .invoice_profile import InvoiceProfile
from .emergency_contact import EmergencyContact
from .travel_document import TravelDocument
from .approver import Approver


@dataclass
class TravelperkExtension:
    invoice_profiles: List[InvoiceProfile]
    emergency_contact: EmergencyContact
    gender: str = None
    date_of_birth: str = None
    travel_policy: str = None
    country_of_residence: str = None
    travel_documents: List[TravelDocument] = None
    approvers: List[Approver] = None
