from pydantic.dataclasses import dataclass


@dataclass
class Manager:
    display_name: str
    value: str = None
    ref: str = None
