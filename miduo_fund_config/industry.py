#!/usr/bin/python
# encoding: utf-8


"""
@description: 米多数据-基金-行业配置
@version: 0.1
@author: zhangl
@contact: zhanglin@miduo.com
@site: https://www.miduo.com
@time: 2016/11/8 12:17
"""
import sys

import MySQLdb
import xlrd

reload(sys)
sys.setdefaultencoding('utf-8')

# conn = MySQLdb.connect(user='test', passwd='test_miduo', host='192.168.4.88', db='hj_wealth_test', charset='utf8')
conn = MySQLdb.connect(user='datagroup', passwd='3d2b4w+2y5n', host='210.14.141.146', db='miduo_db', charset='utf8')
cursor = conn.cursor()


# 资产配置
def industry():
    sql = """
INSERT INTO tbl_fund_industry_config
(fund_code, industry_code, industry_invest, market_value, asset_proportion, report_date, data_source, create_date, create_user)
VALUES ('%s', '%s', '%s', %.2f, %.4f, '2016-09-30 00:00:00', 'Choice', '2016-11-08 00:00:00', 'admin');"""

    workbook = xlrd.open_workbook("D:\PyProject\scripts\miduo_fund_config\data\industry.xls")
    sheet = workbook.sheet_by_index(1)
    nrows = sheet.nrows

    for row in range(1, nrows):
        fund_code = str(sheet.cell(row, 0).value).strip()
        industry_code = str(sheet.cell(row, 1).value).strip()
        industry_invest = str(sheet.cell(row, 2).value).strip()
        market_value = float(sheet.cell(row, 3).value)
        asset_proportion = float(sheet.cell(row, 4).value)

        cursor.execute(sql % (fund_code, industry_code, industry_invest, market_value, asset_proportion))

    conn.commit()
    conn.close()

    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    industry()
    pass
