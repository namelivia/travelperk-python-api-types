from pydantic.dataclasses import dataclass
from typing import List
from .cost_center import CostCenter


@dataclass
class CostCenters:
    offset: int
    limit: int
    cost_centers: List[CostCenter]
