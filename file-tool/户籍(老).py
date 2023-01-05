#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/21
# @Author  : zhangl
import logging

import pandas


def read(path, sheet_name):
    return pandas.read_excel(path, sheet_name=sheet_name)


if __name__ == '__main__':
    df = read("户籍(老).xlsx", sheet_name="区域代码表")
    for index, line in df.iterrows():
        try:
            number = str(int(line['number']))
            # if not number.startswith('65'):
            #     continue

            if number.endswith('0000'):
                province = line['area']
                city = ""
                print(number, province)
                df.loc[index, 'province'] = province
                df.loc[index, 'city'] = ''
                df.loc[index, 'county'] = ''
            elif number.endswith('00'):
                if number.startswith("11") or number.startswith("12") \
                        or number.startswith("50") or number.startswith("31"):
                    city = province
                else:
                    city = line['area'].replace(province, "")
                print(number, province, city)
                df.loc[index, 'province'] = province
                df.loc[index, 'city'] = city
                df.loc[index, 'county'] = ''
            else:
                if number.startswith("11") or number.startswith("12") \
                        or number.startswith("50") or number.startswith("31"):
                    county = line['area'].replace(province, "")
                else:
                    county = line['area'].replace(province + city, "")
                print(number, province, city, county)
                df.loc[index, 'province'] = province
                df.loc[index, 'city'] = city
                df.loc[index, 'county'] = county
            pass


        except Exception as e:
            print(line)
            logging.error(e)
            break

with pandas.ExcelWriter("户籍(老)-处理结果.xlsx") as writer:
    df.to_excel(writer, sheet_name='官方', index=False)
