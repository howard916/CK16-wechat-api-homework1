from .base_api import BaseAPI
import os
import configparser

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = file_path + '/..'
cf = configparser.ConfigParser()
cf.read(f"{project_path}/config.ini")


class ContactsAPIUrls:
    url_access_token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    url_create = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    url_delete = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"


class ContactsAPI(ContactsAPIUrls, BaseAPI):
    def __init__(self):
        self.id = cf.get('config', 'corpid')
        self.secret = cf.get('config', 'corpsecret')
        self.token: str = ''

    def access_token(self):
        url = self.url_access_token
        params = {
            "corpid": self.id,
            "corpsecret": self.secret
        }
        res = self.send('get', url, params=params)
        self.token = res['access_token']

        return res

    def create_contact(self, contact_info):
        url = self.url_create
        params = {'access_token': self.token}
        data = contact_info

        return self.send('post', url, params=params, json=data)

    def delete_contact(self, user_id):
        url = self.url_delete
        params = {
            'access_token': self.token,
            'userid': user_id
        }
        return self.send('get', url, params=params)



