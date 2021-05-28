from travelperk_python_api_types.scim.users.users import Users
from travelperk_python_api_types.scim.users.user import User
from travelperk_python_api_types.scim.users.name import Name
from travelperk_python_api_types.scim.users.phone_number import PhoneNumber
from travelperk_python_api_types.scim.users.meta import Meta
from travelperk_python_api_types.scim.users.enterprise_extension import (
    EnterpriseExtension,
)
from travelperk_python_api_types.scim.users.travelperk_extension import (
    TravelperkExtension,
)
from travelperk_python_api_types.scim.users.invoice_profile import InvoiceProfile
from travelperk_python_api_types.scim.users.emergency_contact import EmergencyContact
from travelperk_python_api_types.scim.users.manager import Manager


class TestSCIM:
    def test_users_entities_are_buildable(self):
        users = Users(
            **{
                "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
                "total_results": 2,
                "items_per_page": 2,
                "start_index": 1,
                "resources": [
                    {
                        "schemas": [
                            "urn:ietf:params:scim:schemas:core:2.0:User",
                            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                            "urn:ietf:params:scim:schemas:extension:travelperk:2.0:User",
                        ],
                        "name": {
                            "given_name": "Marlen",
                            "family_name": "Col",
                            "middle_name": "",
                            "honorific_prefix": "",
                        },
                        "locale": "en",
                        "preferred_language": "en",
                        "title": "Manager",
                        "external_id": "123455667",
                        "id": "29",
                        "groups": [],
                        "active": True,
                        "user_name": "marlen.col@mycompany.com",
                        "phone_numbers": [{"value": "+34 1234567", "type": "work"}],
                        "meta": {
                            "resource_type": "User",
                            "created": "2020-04-01T22:24:44.137082+00:00",
                            "last_modified": "2020-04-01T22:24:44.137082+00:00",
                            "location": "http://app.travelperk.com/api/v2/scim/Users/29",
                        },
                        "enterprise_extension": {
                            "cost_center": "Marketing",
                            "manager": {
                                "value": "123",
                                "ref": "https://app.travelperk.com/api/v2/scim/Users/123/",
                                "display_name": "Jack Jackson",
                            },
                        },
                        "travelperk_extension": {
                            "gender": "M",
                            "date_of_birth": "1980-02-02",
                            "travel_policy": "Marketing travel policy",
                            "invoice_profiles": [{"value": "My Company Ltd"}],
                            "emergency_contact": {
                                "name": "Jane Goodie",
                                "phone": "+34 9874637",
                            },
                        },
                    }
                ],
            }
        )
        assert type(users) is Users
        assert type(users.resources[0]) is User
        assert type(users.resources[0].name) is Name
        assert type(users.resources[0].phone_numbers[0]) is PhoneNumber
        assert type(users.resources[0].meta) is Meta
        assert type(users.resources[0].travelperk_extension) is TravelperkExtension
        assert (
            type(users.resources[0].travelperk_extension.invoice_profiles[0])
            is InvoiceProfile
        )
        assert (
            type(users.resources[0].travelperk_extension.emergency_contact)
            is EmergencyContact
        )
        assert type(users.resources[0].enterprise_extension) is EnterpriseExtension
        assert type(users.resources[0].enterprise_extension.manager) is Manager
