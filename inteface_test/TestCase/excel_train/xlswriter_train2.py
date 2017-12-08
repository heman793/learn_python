# -*- coding:utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook("data.xlsx")
worksheet = workbook.add_worksheet()

data = (
    ['kobe', 5000],
    ['T-Mac', 3000],
    ['Jordan', 6000],
    ['James', 5000],
)

f = workbook.add_format({'bold': True, 'bg_color': 'yellow'})

worksheet.write(0, 0, 'name', f)
worksheet.write(0, 1, 'price', f)

row = 1
col = 0

for item, cost in data:
    worksheet.write(row, col, item)
    worksheet.write(row, col+1, cost)
    row += 1

workbook.close()