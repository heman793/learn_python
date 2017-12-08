# -*- coding:utf-8 -*-

import unittest
import os
import time
import HTMLTestRunner
# import common.send_mail


# 定义用例路径
case_path = os.path.join(os.getcwd(), "TestCase")


# 获取所有case
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    # print discover
    return discover


# 查找最新的测试报告
def getnewestreport(report_dir):
    lists = os.listdir(report_dir)  # 返回指定的文件夹包含的文件或文件夹的名字列表
    print lists
    lists.sort(key=lambda fn: os.path.getatime(report_dir+"\\"+fn))  # 通过sort方法重新按时间对目录下的文件进行排序
    print lists
    filename = os.path.join(report_dir, lists[-1])  # lists[-1]取最新生成的文件或文件夹
    print filename
    return filename

#
if __name__ == '__main__':
    # 定义报告存放路径
    report_path = os.path.join(os.getcwd(), 'report')
    print report_path

    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print now

    # html报告文件路径
    # report_abspath = os.path.join(report_path, "result.html")
    report_abspath = os.path.join(report_path, now+"_result.html")
    # 打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'Inteface testing report, test result as follow：',
                                           description=u'test case exec summary：')
    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()

    # 获取最新报告并通过邮件发送
    # rep = getnewestreport(report_path)
    # common.send_mail.sendattachmail(report_abspath)




    