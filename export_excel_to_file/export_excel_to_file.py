#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 22:23
# @Author  : *
# from  https://blog.csdn.net/bitcarmanlee/article/details/68490125

import xlrd

target = "target.xlsx"


def open_excel(file=target):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as ex:
        print(ex)


def read_sheet(file=target, sheet_index=0):
    data = open_excel(file)
    table = data.sheet_by_index(sheet_index)
    nrows = table.nrows
    ncols = table.ncols

    f = open("result.txt", "w")
    for i in range(nrows):
        line = ""
        for j in range(ncols):
            cell_value = table.cell_value(i, j)  # 得到具体一个cell的值
            if not isinstance(cell_value, str):
                cell_value = str(cell_value)
            line = line + cell_value + ","
        line = line[:-1]
        line = line + "\n"
        print(line)
        f.write(line)
    f.close()


def print_row(file=target, index=0, sheet_index=0):
    data = open_excel(file)
    table = data.sheets()[sheet_index]
    nrows = table.nrows  # 行
    ncols = table.ncols  # 列
    rowdata = table.row_values(index)  # 一行，为一个list
    rowlist = map(lambda x: str(x), rowdata)
    print(",".join(rowlist))


def print_col(file=target, index=0, sheet_index=0):
    data = open_excel(file)
    table = data.sheet_by_index(sheet_index)
    nrows = table.nrows  # 行
    ncols = table.ncols  # 列
    coldata = table.col_values(index)  # 一列，为一个list
    collist = map(lambda x: str(x), coldata)
    print(",".join(collist))


if __name__ == '__main__':
    # print_col(file=target, index=1, sheet_index=1)
    # print_row(file=target, index=1, sheet_index=1)
    # read_sheet(file=target, sheet_index=1)
    pass
