from typing import List
from dataclasses import dataclass
from .category import Category
from .document import Document


@dataclass
class Requirement:
    category: Category
    sub_category: Category
    summary: str
    details: str
    start_date: str
    end_date: str
    documents: List[Document]
