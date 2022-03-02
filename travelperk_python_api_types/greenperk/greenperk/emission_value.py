from pydantic.dataclasses import dataclass


@dataclass
class EmissionValue:
    CO2e_kg: int
