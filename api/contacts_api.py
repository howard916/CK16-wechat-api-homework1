from .base_api import BaseAPI
import os
import configparser

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = file_path + '/..'
cf = configparser.ConfigParser()
cf.read(f"{project_path}/config.ini")


class ContactsAPIUrls:
    url_create = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    url_delete = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
    url_find = "https://qyapi.weixin.qq.com/cgi-bin/user/get"


class ContactsAPI(ContactsAPIUrls, BaseAPI):
    def create_contact(self, contact_info):
        url = self.url_create
        data = contact_info
        return self.send('post', url, json=data)

    def delete_contact(self, user_id):
        url = self.url_delete
        params = {
            'userid': user_id
        }
        return self.send('get', url, params=params)

    def find_contact(self, user_id):
        url = self.url_find
        params = {
            'userid': user_id
        }
        return self.send('get', url, params=params)
