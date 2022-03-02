from pydantic.dataclasses import dataclass
from .emission_value import EmissionValue


@dataclass
class Emissions:
    emissions: EmissionValue
    distance_km: int
