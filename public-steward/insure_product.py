#!/usr/bin/python
# encoding: utf-8


"""
@version: ??
@author: zhangl
@contact: zhanglin@miduo.com
@site: https://www.miduo.com
@time: 2017/7/28 18:02
"""

import sys
import pymysql

import xlrd
sys.setdefaultencoding('utf-8')

host = '192.168.4.82'
user = 'backup'
passwd = 'miduo'
db_name = 'miduo_db'

conn = pymysql.connect(user=user, passwd=passwd, host=host, db=db_name, charset='utf8')
cursor = conn.cursor()


def read_company_map():
    company_map = {}

    cursor.execute("SELECT org_name,id FROM tbl_org_info WHERE org_industry = 2 AND is_deleted = 0")
    org_info_fetchall = cursor.fetchall();
    for org_info in org_info_fetchall:
        # print org_info[0], org_info[1]
        company_map[org_info[0]] = org_info[1]

    return company_map

def read_excel():
    workbook = xlrd.open_workbook("insure2.xlsx")
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows
    for index in range(1, nrows):
        compantName = str(sheet.cell(index, 0).value).strip()
        productName = str(sheet.cell(index, 1).value).strip()
        print(compantName,productName)

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # company_map = read_company_map()
    # print company_map
    read_excel()

    pass
