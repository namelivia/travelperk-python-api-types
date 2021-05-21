from pydantic.dataclasses import dataclass


@dataclass
class InfoSource:
    name: str
    url: str
