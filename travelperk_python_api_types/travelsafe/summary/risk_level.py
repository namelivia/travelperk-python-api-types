from pydantic.dataclasses import dataclass


@dataclass
class RiskLevel:
    id: str
    name: str
    details: str
