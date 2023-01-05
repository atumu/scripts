#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/15
# @Author  : zhangl
import logging

import pandas

df = pandas.read_excel("idcards.xlsx", sheet_name="官方")
for index, row in df.iterrows():
    try:
        code = str(int(row['number']))
        # print(index)
        # if not code.startswith('130'):
        #     continue

        if '0000' in code:
            province = row['area']
            city = ""
            # print(province)
            df.loc[index, 'province'] = province
            df.loc[index, 'city'] = ''
            df.loc[index, 'county'] = ''
        elif code.endswith('00'):
            city = row['area']
            # print(province, city)
            df.loc[index, 'province'] = province
            df.loc[index, 'city'] = city
            df.loc[index, 'county'] = ''
        else:
            county = row['area']
            # print(province, city, county)
            df.loc[index, 'province'] = province
            df.loc[index, 'city'] = city
            df.loc[index, 'county'] = county
    except:
        logging.error(row)
        break

with pandas.ExcelWriter("idcards2.xlsx") as writer:
    df.to_excel(writer, sheet_name='官方', index=False)