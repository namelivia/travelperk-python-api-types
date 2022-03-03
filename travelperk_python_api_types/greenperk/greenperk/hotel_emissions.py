from pydantic.dataclasses import dataclass
from .emission_value import EmissionValue


@dataclass
class HotelEmissions:
    emissions: EmissionValue
