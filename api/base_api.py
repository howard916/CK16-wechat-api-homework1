import requests

import os
import configparser
from .expect_handle import expect_handle

project_path = os.path.dirname(os.path.abspath(__file__)) + "/.."
cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')


class BaseAPI:
    def __init__(self):
        self.id = cf.get('config', 'corpid')
        self.secret = cf.get('config', 'corpsecret')
        self.session = requests.Session()
        self.session.params['access_token'] = self.access_token()['access_token']

    @expect_handle
    def send(self, method, url, **kwargs):
        return self.session.request(method, url, timeout=60, **kwargs)

    def access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self.id,
            "corpsecret": self.secret
        }
        res = self.send('get', url, params=params)
        return res
