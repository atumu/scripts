#!/usr/bin/python
# encoding: utf-8


"""
@version: ??
@author: zhangl
@contact: zhanglin@miduo.com
@site: https://www.miduo.com
@time: 2016/9/28 13:37
"""
import sys

import requests
import xlrd

sys.setdefaultencoding('utf-8')


def read_excel():
    workbook = xlrd.open_workbook("D:/PyProject/scripts/test/insure.xlsx")
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows

    data = []

    for r in range(2, nrows):
        id = int(sheet.cell(r, 0).value)
        name = str(sheet.cell(r, 2).value)
        big = str(sheet.cell(r, 3).value)[0:]
        small = str(sheet.cell(r, 4).value)[0:]
        mobile = str(sheet.cell(r, 5).value)[0:]
        company = {"id": id, "name": name, "big": big, "small": small, "mobile": mobile}
        data.append(company)
    return data


def save_image(company):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    big = requests.get(company['big'], headers=headers, stream=True, timeout=30)
    small = requests.get(company['small'], headers=headers, stream=True, timeout=30)
    mobile = requests.get(company['mobile'], headers=headers, stream=True, timeout=30)

    path = "D:/PyProject/scripts/test/"

    company_name = str(company['id'])
    output = open(path + "big/" + company_name + company['big'][-4:], 'wb')
    output.write(big.content)
    output.close()

    output = open(path + "small/" + company_name + company['small'][-4:], 'wb+')
    output.write(small.content)
    output.close()

    output = open(path + "mobile/" + company_name + company['mobile'][-4:], 'wb+')
    output.write(mobile.content)
    output.close()
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    data = read_excel()

    print(len(data))

    # for company in data:
    #     save_image(company)

    print("运行完成")
