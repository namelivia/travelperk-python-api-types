from dataclasses import dataclass
from .category import Category


@dataclass
class Guideline:
    category: Category
    sub_category: Category
    summary: str
    details: str
    severity: str
