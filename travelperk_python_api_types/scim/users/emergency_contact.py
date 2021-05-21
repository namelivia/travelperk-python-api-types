from pydantic.dataclasses import dataclass


@dataclass
class EmergencyContact:
    name: str = None
    phone: str = None
