from pydantic.dataclasses import dataclass


@dataclass
class Meta:
    resource_type: str
    created: str
    last_modified: str
    location: str
