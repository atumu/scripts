#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 10:28
# @Author  : ZhangL


from datetime import datetime
import os
from decimal import Decimal


import pandas as pd
import xlrd

workbook = xlrd.open_workbook("check.xlsx")
sheets = workbook.sheets()

target = datetime.now().strftime('%Y-%m-%d_%H%M%S')
os.makedirs(target)
print('统计结果将存入:', target)

for sheet in sheets:
    sheet_name = sheet.name
    data = []

    for i in range(1, sheet.nrows):
        date = int(xlrd.xldate_as_datetime(sheet.cell(i, 0).value, 0).strftime('%Y%m%d'))
        name = sheet.cell(i, 5).value
        try:
            value = Decimal(sheet.cell(i, 6).value).quantize(Decimal("0.00"))
            price = Decimal(sheet.cell(i, 10).value).quantize(Decimal("0.00")).__str__()
            data.append({'name': name, 'price': price, 'min': date, 'max': date, 'value': value})
        except:
            print(sheet_name, '第', str(i + 1), '行数据有误，已默认升数为0计入统计', date, name, 'K-单价', sheet.cell(i, 10).value)
            value = Decimal('0').quantize(Decimal("0.00"))
            price = Decimal(sheet.cell(i, 10).value).quantize(Decimal("0.00")).__str__()
            data.append({'name': name, 'price': price, 'min': date, 'max': date, 'value': value})

    df = pd.DataFrame(data)

    df.groupby(['name', 'price']) \
        .agg({'value': 'sum', 'min': 'min', 'max': 'max'}) \
        .to_excel(target + '/' + sheet_name + '.xlsx', sheet_name=sheet_name)
