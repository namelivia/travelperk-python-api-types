from pydantic.dataclasses import dataclass


@dataclass
class Approver:
    display_name: str
    value: str = None
    ref: str = None
    condition: str = None
