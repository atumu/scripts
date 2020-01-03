#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 20:59
# @Author  : ZhangL

import xlrd

filename = "C:/Users/zl409/Desktop/SB00l测试(1).xls"
workbook = xlrd.open_workbook(filename, formatting_info=True)
sheets = workbook.sheet_names()
for index in sheets:
    sheet = workbook.sheet_by_name(index)
    nrow = sheet.nrows
    nclo = sheet.ncols
    keys = []
    for i in range(nrow):
        values = sheet.row_values(i)
        value_p = []
        for m in values:
            if m is not '':
                value_p.append(m)
        keys.append(value_p)

    print(keys)


