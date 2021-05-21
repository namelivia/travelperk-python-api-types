from pydantic.dataclasses import dataclass
from .category import Category


@dataclass
class SafetyMeasure:
    category: Category
    sub_category: Category
    details: str
    summary: str
