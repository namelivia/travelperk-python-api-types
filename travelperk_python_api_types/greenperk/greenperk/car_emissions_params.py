from pydantic.dataclasses import dataclass


@dataclass
class CarEmissionsParams:
    acriss_code: str
    num_days: int
    distance_per_day: int
