# -*- coding:utf-8 -*-
# 批量用例执行--手工加载

import unittest

class TestOne(unittest.TestCase):
    def setUp(self):
        print '\ncases before'
        pass

    def test_add(self):
        '''test add method'''
        print 'add...'
        a = 3 + 4
        b = 7
        self.assertEqual(a, b)

    def test_sub(self):
        '''test sub method'''
        print 'sub...'
        a = 10 - 5
        b = 5
        self.assertEqual(a, b)

    def tearDown(self):
        print 'case after'
        pass

if __name__ == '__main__':
    # 1、构造用例集
    suite = unittest.TestSuite()

    # 2、执行顺序是安加载顺序：先执行test_sub，再执行test_add
    suite.addTest(TestOne("test_sub"))
    suite.addTest(TestOne("test_add"))

    # 3、实例化runner类
    runner = unittest.TextTestRunner()
    # 4、执行测试
    runner.run(suite)
