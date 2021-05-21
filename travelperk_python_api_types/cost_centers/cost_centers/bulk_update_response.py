from pydantic.dataclasses import dataclass


@dataclass
class BulkUpdateResponse:
    updated_count: int
