from pydantic.dataclasses import dataclass


@dataclass
class TrainEmissionsParams:
    origin_id: str
    destination_id: str
    vendor: str
