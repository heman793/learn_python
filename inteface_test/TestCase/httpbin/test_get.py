# -*- coding:utf-8 -*-

import unittest
from common import base
from common import HTTPService


class TestGet(unittest.TestCase):
    '''test get inteface'''

    def setUp(self):
        print '\ncase before--get'
        self.url = base.get_url("get")

    def test_get(self):
        u'''test get'''
        # r = requests.get(self.url)
        r = HTTPService.MyHTTP().send_request(self.url, "get")
        print r
        self.assertEqual(r["url"], "http://httpbin.org/get")

    def test_get_with_headers(self):
        u'''test get with headers'''
        headers = {
                    "User-Agent": "test request headers"
        }

        # r = requests.get(self.url, headers=headers)
        r = HTTPService.MyHTTP().send_request(self.url, "get", headers=headers)
        print r
        self.assertEqual(r["headers"]["User-Agent"], headers["User-Agent"])

    def test_get_with_params(self):
        u'''test get with params'''
        params = {
                    "show_env": "1"
        }

        # r = requests.post(self.url, params=params)
        r = HTTPService.MyHTTP().send_request(self.url, "get", params=params)
        print r["url"]
        self.assertEqual(r["args"]["show_env"], "1")

    def test_get_with_headers_and_params(self):
        u'''test get with headers and params'''
        headers = {
                    "User-Agent": "test request headers"
        }

        params = {
                    "show_env": "1"
        }

        r = HTTPService.MyHTTP().send_request(self.url, "get", headers=headers, params=params)
        print r

    def tearDown(self):
        print 'case after--get'

if __name__ == '__main__':
    unittest.main()