from pydantic.dataclasses import dataclass


@dataclass
class Document:
    name: str
    document_url: str
    download_url: str = None
