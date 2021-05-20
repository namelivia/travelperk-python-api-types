from dataclasses import dataclass
from typing import List
from .cost_center import CostCenter


@dataclass
class CostCenters:
    offset: int
    limit: int
    total: int
    cost_centers: List[CostCenter]
