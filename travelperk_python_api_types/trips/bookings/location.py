from dataclasses import dataclass


@dataclass
class Location:
    latitude: str
    longitude: str
    iata_code: str = None
