from pydantic.dataclasses import dataclass


@dataclass
class Name:
    first_name: str
    last_name: str
    middle_name: str
    title: str
