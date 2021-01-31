import pytest
from api import ContactsAPI

@pytest.fixture()
def mock_users():
    def _mock_users(users_info: list):
        for user in users_info:
            ContactsAPI().create_contact(user)

    return _mock_users

