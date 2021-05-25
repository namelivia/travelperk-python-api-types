from pydantic.dataclasses import dataclass
from travelperk_python_api_types.travelsafe.category import Category


@dataclass
class SafetyMeasure:
    category: Category
    sub_category: Category
    details: str
    summary: str
