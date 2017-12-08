# -*- coding:utf-8 -*-
# 批量用例执行--自动加载

import unittest
import os


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
    # 1、设置待执行用例的目录
    test_dir = os.path.join(os.getcwd())

    # 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    # 实例化TextTestRunner类
    runner = unittest.TextTestRunner()

    # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)
