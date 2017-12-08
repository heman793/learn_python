import requests
import config


class MyHTTP(object):
    def __init__(self):
        self.url = config.get_host()

    def send_request(self, url, method, **kwargs):
        resp = requests.request(method, url, **kwargs)
        return resp.json()
