#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","123456","inteface")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select * from person")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
print "Person:",data

# 关闭数据库连接
db.close()