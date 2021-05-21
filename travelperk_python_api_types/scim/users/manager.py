from pydantic.dataclasses import dataclass


@dataclass
class Manager:
    value: str = None
    ref: str = None
    display_name: str
