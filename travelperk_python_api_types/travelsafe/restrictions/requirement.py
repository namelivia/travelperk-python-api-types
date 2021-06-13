from typing import List, Optional
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
    end_date: Optional[str]
    documents: List[Document]
