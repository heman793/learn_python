# -*- coding:utf-8 -*-

import xlsxwriter
import time
import datetime

# 创建文件
workbook = xlsxwriter.Workbook("new_excel.xlsx")

# 创建sheet
worksheet = workbook.add_worksheet("first_sheet")

# 写入数据
worksheet.write('A1', 'write something')
worksheet.write(1, 0, 'hello world')

# 设置行属性，行高设置为40
worksheet.set_row(0, 40)

# 设置行属性，把A到B列宽设置为20
worksheet.set_column('A:B', 20)

# 自定义格式
f = workbook.add_format({'border': 1, 'font_size': 13, 'bold': True, 'align': 'center','bg_color': 'cccccc'})
worksheet.write('A3', "python excel", f)
worksheet.set_row(0, 40, f)
worksheet.set_column('A:E', 20, f)

# 写入数字和函数
worksheet.write(0, 1, 32)
worksheet.write(1, 1, 32.3)
worksheet.write(2, 1, '=sum(B1:B2)')

# 写入日期
d = workbook.add_format({'num_format': 'yyyy-mm-dd'})
worksheet.write(0, 2, datetime.datetime.strptime('2017-09-13', '%Y-%m-%d'), d)

# 插入图片
worksheet.insert_image(0, 5, 'test.png')
worksheet.insert_image(0, 5, 'test.png', {'url': 'http://httpbin.org/'})

# 批量往单元格写入数据
worksheet.write_column('A15', [1, 2, 3, 4, 5])  # 列写入，从A15开始
worksheet.write_row('A12', [6, 7, 8, 9])        # 行写入，从A12开始

# 合并单元格写入
worksheet.merge_range(7,5, 11, 8, 'merge_range')

# 关闭文件
workbook.close()