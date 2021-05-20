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


class TestBuilding:
    def test_root_entities_are_buildable(self):
        assert type(CostCenters(2, 3, 12, [])) is CostCenters
        assert type(CostCenterDetail(1, "test", False, 3)) is CostCenterDetail
        assert type(CostCenter(1, "test", 3)) is CostCenter
        assert type(BulkUpdateResponse(1)) is BulkUpdateResponse
