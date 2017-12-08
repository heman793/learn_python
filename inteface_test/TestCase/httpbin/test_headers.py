import requests
import unittest
from common import base


class TestHeaders(unittest.TestCase):
    '''test headers intef   ace'''

    def setUp(self):
        print 'case before--headers'
        self.url = base.get_url("headers")

    def test_headers(self):
        '''test get'''
        r = requests.get(self.url)
        print r.json()
        self.assertEqual(r.json()['headers']['Host'], 'httpbin.org')

    def tearDown(self):
        print 'case after--headers'


if __name__ == '__main__':
    unittest.main()