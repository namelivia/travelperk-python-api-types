from pydantic.dataclasses import dataclass


@dataclass
class Location:
    name: str
    address: str
    latitude: str
    longitude: str
    iata_code: str = None
