# -*- coding:utf-8 -*-
# 单个用例执行
# 1、导入模块
import unittest


# 2、继承自unittest.TestCase类
class TestOne(unittest.TestCase):
    # 3、setUp主要是进行测试前的初始化工作，比如在接口测试前面做一些前置的参数赋值，数据库操作等等
    def setUp(self):
        print '\ncases before'
        pass

    # 4、定义测试用例，名字以“test”开头
    def test_add(self):
        '''test add method'''
        print 'add...'
        a = 3 + 4
        b = 7

        # 5、定义assert断言，判断测试结果
        self.assertEqual(a, b)

    def test_sub(self):
        '''test sub method'''
        print 'sub...'
        a = 10 - 5
        b = 5
        self.assertEqual(a, b)

    # 6、清理环境
    def tearDown(self):
        print 'case after'
        pass

# 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
if __name__ == '__main__':
    unittest.main()
