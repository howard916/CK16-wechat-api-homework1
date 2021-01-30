import requests
import os
import configparser
from .expect_handle import expect_handle

project_path = os.path.dirname(os.path.abspath(__file__)) + "/.."
cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')


class BaseAPI:
    @expect_handle
    def send(self, method, url, **kwargs):
        return requests.request(method, url, timeout=60, **kwargs)

    def data_file_name(self):
        server_type = cf.get('server', 'server_type')
        if server_type == '1':
            return 'data_uso.yaml'
        elif server_type == '2':
            return 'data_usd.yaml'
        else:
            return 'data_aliy.yaml'



