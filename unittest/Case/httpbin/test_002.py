import requests
import unittest


class Test(unittest.TestCase):

    host = 'http://httpbin.org/'

    def setUp(self):
        print '\n'
        print 'case before'
        pass

    def test_useragent(self):
        '''test ip'''
        endpoint = 'user-agent'
        url = ''.join([self.host, endpoint])
        r = requests.get(url)
        print r.json()
        self.assertEqual(r.status_code,200)

    def test_headers(self):
        '''test get'''
        endpoint = 'headers'
        url = ''.join([self.host, endpoint])
        r = requests.get(url)
        print r.json()
        self.assertEqual(r.json()['headers']['Host'], 'httpbin.org')

    def tearDown(self):
        print 'case after'
        pass

if __name__ == '__main__':
    unittest.main()