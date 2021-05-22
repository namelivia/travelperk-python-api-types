from pydantic.dataclasses import dataclass


@dataclass
class Vendor:
    name: str
    code: str = None
