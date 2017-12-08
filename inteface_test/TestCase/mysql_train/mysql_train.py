# -*- coding:utf-8 -*-

import pymysql
from common import config


# 创建连接、游标
conn = pymysql.connect(**config.sql_conn_dict)
cur = conn.cursor()

# 数据库操作
# 方法一：一个参数，直接写在sql语句中
# sql = "select * from person where id = '5'"

# 方法二：一个参数，sql使用参数化传递查询条件
# id = 3
# sql = "select * from person where id = %s " %id

# # 方法三：一个参数，查询条件放在执行语句中
# id = 3
# sql = "select * from person where id = %s "
# rows = cur.execute(sql, id)
# print cur.fetchone()  # 从当前游标开始，取一行


# 一个参数多个值，查询条件放在执行语句中
# id = ('2', '3', '5')
# id = (2, 3, 5)
# sql = "select * from person where id = %s "
#
# rows = cur.executemany(sql, id)
# print cur.fetchall()

# 多个参数多个值，查询条件放在执行语句中
param = [('3', 'kobe'), ('7', 'aaa')]
sql = "select * from person where id = %s and name = %s"

rows = cur.executemany(sql, param)
print cur.fetchall()

# 关闭游标、连接
cur.close()
conn.close()