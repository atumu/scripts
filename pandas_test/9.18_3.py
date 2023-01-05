#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/21
# @Author  : zhangl
import logging

import pandas

if __name__ == '__main__':
    officialDataFrame = pandas.read_excel("户籍(老)-处理结果4.xlsx", sheet_name="官方").fillna('')
    official = {}
    for index, row in officialDataFrame.iterrows():
        try:
            official[str(row['number'])] = (row['province'], row['city'], row['county'])
        except Exception as e:
            print(row)
            logging.error(e)
            break

    df = pandas.read_excel("9.18_3.xlsx", sheet_name="Sheet1")
    print(df)
    not_found_count = 0
    for index, row in df.iterrows():
        number = row['被保人证件号前六位'].replace("*", "")
        number_final = number

        if number_final not in official:
            number_final = number[0:4] + '00'

        if number_final not in official:
            number_final = number[0:2] + '0000'

        if number_final in official:
            if index % 1000 == 0:
                print(index, number, official[number_final])
            df.loc[index, '省'] = official[number_final][0]
            df.loc[index, '市'] = official[number_final][1]
            df.loc[index, '县'] = official[number_final][2]
        else:
            print(index, number, number_final)
            not_found_count = not_found_count + 1

    print(df)
    print("未能匹配数量: " + str(not_found_count))

    with pandas.ExcelWriter("9.18_3-处理结果4.xlsx") as writer:
        df.to_excel(writer, sheet_name='结果', index=False)
