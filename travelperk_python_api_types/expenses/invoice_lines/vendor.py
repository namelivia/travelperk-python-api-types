from pydantic.dataclasses import dataclass


@dataclass
class Vendor:
    code: str = None
    name: str
