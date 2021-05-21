from pydantic.dataclasses import dataclass


@dataclass
class Category:
    id: str
    name: str
