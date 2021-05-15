from dataclasses import dataclass


@dataclass
class Event:
    name: str
    topic: str
