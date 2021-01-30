import pytest
from api import ContactsAPI
import yaml
import os
from allure import feature, story

file_path = os.path.dirname(os.path.abspath(__file__))
test_data = yaml.safe_load(open(f'{file_path}/contacts.yaml', 'r'))

@feature("企业微信联系人API")
class TestContacts:
    @classmethod
    def setup_class(cls):
        cls.api = ContactsAPI()

    @story("Token获取验证")
    def test_access_token(self):
        res = self.api.access_token()
        assert res['errcode'] == 0
        assert res['errmsg'] == 'ok'

    @story("创建联系人")
    @pytest.mark.parametrize('contact_info', test_data['create_contacts'])
    def test_create_contact(self, contact_info):
        res = self.api.create_contact(contact_info)
        assert res == {"errcode": 0, "errmsg": "created"}

    @story("删除联系人")
    @pytest.mark.parametrize('user_id', test_data['delete_contacts'])
    def test_delete_contact(self, user_id):
        res = self.api.delete_contact(user_id)
        assert res == {"errcode": 0, "errmsg": "deleted"}
