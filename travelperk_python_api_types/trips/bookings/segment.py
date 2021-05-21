from pydantic.dataclasses import dataclass
from .origin import Origin
from .destination import Destination


@dataclass
class Segment:
    origin: Origin
    destination: Destination
    external_id: str
