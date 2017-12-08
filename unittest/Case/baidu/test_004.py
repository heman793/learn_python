import requests
import unittest


class Test(unittest.TestCase):

    host = 'https://www.baidu.com/'

    def setUp(self):
        print '\n'
        print 'case before'
        pass

    def test_baidu3(self):
        print 'test baidu 3'

    def test_baidu4(self):
        print 'test baidu 4'

    def tearDown(self):
        print 'case after'
        pass

if __name__ == '__main__':
    unittest.main()