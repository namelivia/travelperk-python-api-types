from travelperk_python_api_types.users.users.users import Users
from travelperk_python_api_types.users.users.user import User


class TestUsers:
    def test_users_entities_are_buildable(self):
        users = Users(
            **{
                "users": [
                    {
                        "id": "8",
                        "user_name": "boss@test.com",
                        "name": {
                            "last_name": "Morrison",
                            "first_name": "Boss",
                            "middle_name": "",
                            "title": "MR",
                        },
                        "preferred_language": "en",
                        "locale": "en-gb",
                        "active": True,
                        "job_title": "Boss",
                        "phone_numbers": ["+34 123456789"],
                        "emergency_contact": {
                            "name": "Mrs. Morrison",
                            "phone": "+34 987654321",
                        },
                    },
                    {
                        "id": "7",
                        "user_name": "manager@test.com",
                        "name": {
                            "last_name": "Roberts",
                            "first_name": "Manager",
                            "middle_name": "",
                            "title": "MRS",
                        },
                        "preferred_language": "en",
                        "locale": "en-gb",
                        "active": True,
                        "job_title": "Office Manager",
                        "phone_numbers": [],
                        "emergency_contact": None,
                    },
                ],
                "limit": 10,
                "offset": 0,
                "total": 2,
            }
        )
        assert type(users) is Users
        assert type(users.users[0]) is User
