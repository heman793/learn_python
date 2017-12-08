import requests
import unittest


class Test(unittest.TestCase):

    host = 'http://httpbin.org/'

    def setUp(self):
        print '\n'
        print 'case before'
        pass

    def test_ip(self):
        u'''test ip'''
        endpoint = 'ip'
        url = ''.join([self.host, endpoint])
        r = requests.get(url)
        print r.json()
        self.assertEqual(r.json()['origin'], '183.63.51.77')

    def test_get(self):
        u'''test get'''
        endpoint = 'get'
        url = ''.join([self.host, endpoint])
        r = requests.get(url)
        print url
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        print 'case after'
        pass

if __name__ == '__main__':
    unittest.main()