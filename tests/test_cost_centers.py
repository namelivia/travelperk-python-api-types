from travelperk_python_api_types.cost_centers.cost_centers.cost_centers import (
    CostCenters,
)
from travelperk_python_api_types.cost_centers.cost_centers.cost_center_detail import (
    CostCenterDetail,
)
from travelperk_python_api_types.cost_centers.cost_centers.cost_center import CostCenter
from travelperk_python_api_types.cost_centers.cost_centers.bulk_update_response import (
    BulkUpdateResponse,
)
from travelperk_python_api_types.expenses.invoice_lines.vendor import Vendor


class TestCostCenters:
    def test_cost_center_entities_are_buildable(self):
        assert type(CostCenters(2, 3, [])) is CostCenters
        assert type(CostCenterDetail(1, "test", False, [], 3)) is CostCenterDetail
        assert type(CostCenter(1, "test", 3)) is CostCenter
        assert type(BulkUpdateResponse(1)) is BulkUpdateResponse

        # Building nesting dictionaries
        cost_centers = CostCenters(
            **{
                "offset": 2,
                "limit": 3,
                "cost_centers": [
                    {
                        "id": 1,
                        "name": "test",
                        "count_users": 15,
                    }
                ],
            }
        )
        assert type(cost_centers) is CostCenters
        assert type(cost_centers.cost_centers[0]) is CostCenter
        assert type(Vendor("test")) is Vendor

    def test_expenses_entities_are_buildable(self):
        assert type(CostCenters(2, 3, [])) is CostCenters
        assert type(CostCenterDetail(1, "test", False, [], 3)) is CostCenterDetail
        assert type(CostCenter(1, "test", 3)) is CostCenter
        assert type(BulkUpdateResponse(1)) is BulkUpdateResponse

        # Building nesting dictionaries
        cost_centers = CostCenters(
            **{
                "offset": 2,
                "limit": 3,
                "cost_centers": [
                    {
                        "id": 1,
                        "name": "test",
                        "count_users": 15,
                    }
                ],
            }
        )
        assert type(cost_centers) is CostCenters
        assert type(cost_centers.cost_centers[0]) is CostCenter
        assert type(Vendor("test")) is Vendor
