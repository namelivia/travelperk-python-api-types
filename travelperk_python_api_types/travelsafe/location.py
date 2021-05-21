from pydantic.dataclasses import dataclass


@dataclass
class Location:
    name: str
    type: str
    country_code: str
