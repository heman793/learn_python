import requests
import unittest


class Test(unittest.TestCase):

    host = 'https://www.baidu.com/'

    def setUp(self):
        print '\n'
        print 'case before'
        pass

    def test_baidu1(self):
        print 'test baidu 1'

    def test_baidu2(self):
        print 'test baidu 2'

    def tearDown(self):
        print 'case after'
        pass

if __name__ == '__main__':
    unittest.main()