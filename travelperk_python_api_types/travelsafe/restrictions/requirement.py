from typing import List
from pydantic.dataclasses import dataclass
from travelperk_python_api_types.travelsafe.category import Category
from .document import Document


@dataclass
class Requirement:
    category: Category
    sub_category: Category
    summary: str
    details: str
    start_date: str
    documents: List[Document]
    end_date: str = None
