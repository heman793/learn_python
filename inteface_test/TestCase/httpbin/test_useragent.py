import requests
import unittest
from common import base


class TestUserAgent(unittest.TestCase):
    '''test useragent inteface'''

    def setUp(self):
        print 'case before--headers'
        self.url = base.get_url("user-agent")

    def test_useragent(self):
        '''test uaeragent'''
        r = requests.get(self.url)
        print r.json()
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        print 'case after--headers'

if __name__ == '__main__':
    unittest.main()