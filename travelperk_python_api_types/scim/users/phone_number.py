from pydantic.dataclasses import dataclass


@dataclass
class PhoneNumber:
    value: str
    type: str
