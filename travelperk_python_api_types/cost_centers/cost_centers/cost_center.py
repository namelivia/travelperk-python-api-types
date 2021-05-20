from dataclasses import dataclass


@dataclass
class CostCenter:
    id: int
    name: str
    count_users: int
