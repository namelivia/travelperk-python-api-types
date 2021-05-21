from pydantic.dataclasses import dataclass


@dataclass
class Name:
    given_name: str
    family_name: str
    middle_name: str
    honorific_prefix: str
