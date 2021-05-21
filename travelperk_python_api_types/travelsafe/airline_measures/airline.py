from pydantic.dataclasses import dataclass


@dataclass
class Airline:
    name: str
    iata_code: str
