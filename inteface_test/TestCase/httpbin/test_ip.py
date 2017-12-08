import requests
import unittest
from common import base


class TestIp(unittest.TestCase):
    '''test ip inteface'''

    def setUp(self):
        print 'case before--ip'
        self.url = base.get_url("ip")

    def test_ip(self):
        u'''test ip'''
        r = requests.get(self.url)
        print r.json()
        self.assertEqual(r.json()['origin'], '183.131.161.74')

    def tearDown(self):
        print 'case after--ip'

if __name__ == '__main__':
    unittest.main()