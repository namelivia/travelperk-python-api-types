from pydantic.dataclasses import dataclass


@dataclass
class HotelEmissionsParams:
    country_code: str
    num_days: int
