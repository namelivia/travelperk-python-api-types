from pydantic.dataclasses import dataclass


@dataclass
class FlightEmissionsParams:
    origin: str
    destination: str
    cabin_class: str
    airline_code: str
