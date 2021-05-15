from dataclasses import dataclass


@dataclass
class User:
    fist_name: str
    last_name: str
    email: str
    id: int
    phone: str = None
    profile_picture: str = None
