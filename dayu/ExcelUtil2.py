#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/15
import time
import warnings

import openpyxl

warnings.simplefilter("ignore")


def read(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.worksheets[0]
    data_list = []
    for row in sheet.rows:

        # 如果姓名为空 或者 姓名不是数组
        if row[3] is None or row[3].value is None \
                or len(row[3].value.strip()) == 0 \
                or "[\"" not in row[3].value:
            row_list = []
            for cell in row:
                row_list.append(str(cell.value).strip())
            # print(row_list)
            data_list.append(row_list)

        else:  # 姓名是数组
            # print(row[0].value, row[3].value)
            XINGMING = clean(row[3].value)
            ZJHM = clean(row[4].value)
            JCEHJ = clean(row[5].value)
            GJLB = clean(row[9].value)
            if len(XINGMING) != len(ZJHM) or len(ZJHM) != len(JCEHJ) or len(JCEHJ) != len(GJLB):
                print(row[0].value, "渣渣数据")
                continue
            for i in range(len(XINGMING)):
                row_list = []
                row_list.append(str(row[0].value).strip())
                row_list.append(str(row[1].value).strip())
                row_list.append(str(row[2].value).strip())
                row_list.append(str(XINGMING[i]).strip())
                row_list.append(str(ZJHM[i]).strip())
                row_list.append(str(JCEHJ[i]).strip())
                row_list.append(str(row[6].value).strip())
                row_list.append(str(row[7].value).strip())
                row_list.append(str(row[8].value).strip())
                row_list.append(str(GJLB[i]).strip())
                data_list.append(row_list)
    return data_list


def clean(value):
    return value.replace(']', '').replace('[', '').replace("\"", "").split(',')


def write(list, path):
    path = path % time.strftime("%Y%m%d%H%M%S", time.localtime())
    workbook = openpyxl.Workbook()
    sheet = workbook.get_sheet_by_name("Sheet")
    for row in list:
        sheet.append(row)
    workbook.save(path)


if __name__ == '__main__':
    list = read(path="data/汇缴补缴明细.xlsx")
    for line in list[0:100]:
        print(line)
    write(list=list, path="data/汇缴补缴明细-%s.xlsx")
