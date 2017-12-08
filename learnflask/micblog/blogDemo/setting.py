# -*- coding: utf-8 -*-

# 是否开始调试模式
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

# session必须要设置key
SECRET_KEY='QAZWSXEDCRFVTGB~!@#$%^'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/inteface"