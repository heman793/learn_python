# -*- coding:utf-8 -*-

import xlrd
import os
from datetime import date,datetime


filename = "demo.xlsx"
filePath = os.path.join(os.getcwd(), filename)

print filePath

# 1、打开文件
x1 = xlrd.open_workbook(filePath)

# 2、获取sheet对象
# print 'sheet_names:', x1.sheet_names()  # 获取所有sheet名字
# print 'sheet_number:', x1.nsheets        # 获取sheet数量
# print 'sheet_object:', x1.sheets()       # 获取所有sheet对象
# print 'By_name:', x1.sheet_by_name("test")  # 通过sheet名查找
# print 'By_index:', x1.sheet_by_index(3)  # 通过索引查找

# 3、获取sheet的汇总数据
sheet1 = x1.sheet_by_name("plan")
# print "sheet name:", sheet1.name   # get sheet name
# print "row num:", sheet1.nrows  # get sheet all rows number
# print "col num:", sheet1.ncols  # get sheet all columns number

# 4、单元格批量读取
# 4.1 行操作
# print sheet1.row_values(0)  # 获取第一行所有内容，合并单元格，首行显示值，其它为空。
# print sheet1.row(0)         # 获取单元格值类型和内容
# print sheet1.row_types(0)   # 获取单元格数据类型

# 4.2列操作
# print sheet1.row_values(0, 6, 10)   # 取第1行，第6~10列（不含第10表）
# print sheet1.col_values(0, 0, 5)    # 取第1列，第0~5行（不含第5行）
# print sheet1.row_slice(2, 0, 2)     # 获取单元格值类型和内容
# print sheet1.row_types(1, 0, 2)   # 获取单元格数据类型


# 5、特定单元格读取
# 5.1 取值
# print sheet1.cell_value(1, 2)
# print sheet1.cell(1, 2).value
# print sheet1.row(1)[2].value
# 5.1 取类型
# print sheet1.cell(1, 2).ctype
# print sheet1.cell_type(1, 2)
# print sheet1.row(1)[2].ctype

# 6、(0,0)转换成A1
# print xlrd.cellname(0, 0)   # (0,0)转换成A1
# print xlrd.cellnameabs(0, 0) # (0,0)转换成$A$1
# print xlrd.colname(30)  # 把列由数字转换为字母表示


def read_excel(sheet, row, col):
    name = sheet.cell_value(row, col)
    type = sheet.cell_type(row, col)

    if type == 0:
        name = "''"
    elif type == 1:
        name = name
    elif type == 2 and name % 1 == 0:
        name = int(name)
    elif type == 3:
        # 方法一：转换为日期时间
        # date_value = xlrd.xldate.xldate_as_datetime(name, 0)
        # name = date_value
        # 方法二：转换为无组
        date_value = xlrd.xldate_as_tuple(name, 0)
        name = datetime(*date_value).strftime('%Y-%m-%d %H:%M:%:%S')

    elif type == 4:
        name = True if name == 1 else False
    return name

# 7、获取表格里不同类型的name
print sheet1.cell_value(0, 7)   # 空 0
print sheet1.cell_type(0, 7)
print read_excel(sheet1, 0, 7)

print sheet1.cell_value(0, 0)   # 字符串 1
print sheet1.cell_type(0, 0)
print read_excel(sheet1, 0, 0)

print sheet1.cell_value(0, 8)   # 数字 2
print sheet1.cell_type(0, 8)
print read_excel(sheet1, 0, 8)

print sheet1.cell_value(0, 9)   # 日期 3
print sheet1.cell_type(0, 9)
print read_excel(sheet1, 0, 9)

print sheet1.cell_value(0, 10)   # 布尔 4
print sheet1.cell_type(0, 10)
print read_excel(sheet1, 0, 10)
