from pydantic.dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    id: int
    profile_picture: str = None
    phone: str = None
