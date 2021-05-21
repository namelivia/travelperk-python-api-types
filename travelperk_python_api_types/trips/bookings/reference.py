from pydantic.dataclasses import dataclass


@dataclass
class Reference:
    type: str
    value: str
