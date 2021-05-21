from pydantic.dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    external_id: str = None
