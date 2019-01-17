#!/usr/bin/python
# encoding: utf-8


"""
@description: 米多数据-基金-资产配置
@version: 0.1
@author: zhangl
@contact: zhanglin@miduo.com
@site: https://www.miduo.com
@time: 2016/11/8 12:17
"""
import sys

import MySQLdb
import xlrd

sys.setdefaultencoding('utf-8')



# conn = MySQLdb.connect(user='test', passwd='test_miduo', host='192.168.4.88', db='hj_wealth_test', charset='utf8')
conn = MySQLdb.connect(user='datagroup', passwd='3d2b4w+2y5n', host='210.14.141.146', db='miduo_db', charset='utf8')
cursor = conn.cursor()

# 资产配置
def distribution():
    sql = """
INSERT INTO tbl_fund_distribution_config
(fund_code, trading_date, equities_val, equities_rate, tdr_val, tdr_rate, fi_val, fi_rate,
bond_val, bond_rate, abs_val, abs_rate, di_val, di_rate, rmcfs_val, rmcfs_rate, mmi_val,
mmi_rate, bdasc_val, bdasc_rate, aoa_val, aoa_rate, create_date, create_user)
VALUES ('%s', '%s', %.2f, %.2f, %.2f, %.2f, %.2f, %.2f,
%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f,
%.2f, %.2f, %.2f, %.2f, %.2f, '2016-11-08 00:00:00', 'admin');"""

    workbook = xlrd.open_workbook("D:\PyProject\scripts\miduo_fund_config\data\distribution.xls")
    sheet = workbook.sheet_by_index(1)
    nrows = sheet.nrows

    for row in range(2, nrows):
        fund_code = str(sheet.cell(row, 0).value).strip()
        trading_date = str(sheet.cell(row, 1).value).strip()
        equities_val = float(sheet.cell(row, 2).value)
        equities_rate = float(sheet.cell(row, 3).value)
        tdr_val = float(sheet.cell(row, 4).value)
        tdr_rate = float(sheet.cell(row, 5).value)
        fi_val = float(sheet.cell(row, 6).value)
        fi_rate = float(sheet.cell(row, 7).value)
        bond_val = float(sheet.cell(row, 8).value)
        bond_rate = float(sheet.cell(row, 9).value)
        abs_val = float(sheet.cell(row, 10).value)
        abs_rate = float(sheet.cell(row, 11).value)
        di_val = float(sheet.cell(row, 12).value)
        di_rate = float(sheet.cell(row, 13).value)
        rmcfs_val = float(sheet.cell(row, 14).value)
        rmcfs_rate = float(sheet.cell(row, 15).value)
        mmi_val = float(sheet.cell(row, 16).value)
        mmi_rate = float(sheet.cell(row, 17).value)
        bdasc_val = float(sheet.cell(row, 18).value)
        bdasc_rate = float(sheet.cell(row, 19).value)
        aoa_val = float(sheet.cell(row, 20).value)
        aoa_rate = float(sheet.cell(row, 21).value)

        cursor.execute( sql%(fund_code,trading_date,equities_val,equities_rate,tdr_val,tdr_rate,fi_val,fi_rate, bond_val,
                   bond_rate, abs_val, abs_rate, di_val, di_rate, rmcfs_val, rmcfs_rate, mmi_val,
                   mmi_rate, bdasc_val,bdasc_rate, aoa_val, aoa_rate))

    conn.commit()
    conn.close()

    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    distribution()

    pass
