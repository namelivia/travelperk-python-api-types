from pydantic.dataclasses import dataclass
from travelperk_python_api_types.travelsafe.category import Category


@dataclass
class Guideline:
    category: Category
    sub_category: Category
    summary: str
    details: str
    severity: str
