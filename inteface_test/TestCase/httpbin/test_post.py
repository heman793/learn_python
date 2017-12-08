# -*- coding:utf-8 -*-

import unittest
from common import base
from common import HTTPService
import os


class TestPost(unittest.TestCase):
    '''test post inteface'''

    def setUp(self):
        print 'case before--post'
        self.url = base.get_url("post")

    def test_post_with_headers(self):
        u'''test get with headers'''
        headers = {
                    "User-Agent": "test request headers"
        }

        # r = requests.post(self.url, headers=headers)
        r = HTTPService.MyHTTP().send_request(self.url, "post", headers=headers)
        print r
        self.assertEqual(r["headers"]["User-Agent"], headers["User-Agent"])

    def test_post_with_data(self):
        data = {
                'key1': 'value1',
                'key2': 'value2'
        }

        # r = requests.post(self.url, data=data)
        r = HTTPService.MyHTTP().send_request(self.url, "post", data=data)
        print r
        self.assertEqual(r["form"]["key2"], "value2")

    def test_post_with_params(self):
        params = {
                'key3': 'params3',
                'key4': 'params4'
        }

        # r = requests.post(self.url, params=params)
        r = HTTPService.MyHTTP().send_request(self.url, "post", params=params)
        print r
        self.assertEqual(r["args"]["key3"], "params3")

    def test_post_with_json(self):
        json = {
            "sites": [
                {"name": "test", "url": "www.test.com"},
                {"name": "google", "url": "www.google.com"},
                {"name": "weibo", "url": "www.weibo.com"}
            ]
        }

        # r = requests.post(self.url, json=json)
        r = HTTPService.MyHTTP().send_request(self.url, "post", json=json)
        print r
        self.assertEqual(r["json"]["sites"][0]["name"], "test")

    def test_post_with_file(self):
        # 普通上传
        file_path = os.path.join(os.getcwd(), "TestCase/httpbin/test.txt")
        files = {
            'file': open(file_path, 'rb')
        }

        #  r = requests.post(self.url, files=files)
        r = HTTPService.MyHTTP().send_request(self.url, "post", files=files)
        print r
        self.assertEqual(r["files"]["file"], "hello world!\n")

    def test_post_with_kwargs(self):
        headers = {
            "User-Agent": "test request headers"
        }
        data = {
            'key1': 'value1',
            'key2': 'value2'
        }
        params = {
            'key3': 'params1',
            'key4': 'params2'
        }
        file_path = os.path.join(os.getcwd(), "TestCase/httpbin/test.txt")
        files = {
            'file': open(file_path, 'rb')
        }

        r = HTTPService.MyHTTP().send_request(self.url, "post", data=data, params=params,
                                              headers=headers, files=files)
        print r

    def tearDown(self):
        print 'case after--post'

if __name__ == '__main__':
    unittest.main()