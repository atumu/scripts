#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/21
# @Author  : zhangl
import logging

import pandas


def read(path, sheet_name):
    return pandas.read_excel(path, sheet_name=sheet_name)


def fix():
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


def sort_by_number():
    df = read("户籍(老)-处理结果.xlsx", sheet_name="官方")
    df = df.sort_values(by=['number'])

    with pandas.ExcelWriter("户籍(老)-处理结果2.xlsx") as writer:
        df.to_excel(writer, sheet_name='官方', index=False)


def get_office_dic():
    officialDataFrame = pandas.read_excel("户籍(老)-处理结果.xlsx", sheet_name="官方").fillna('')
    official = {}
    for index, row in officialDataFrame.iterrows():
        official[str(row['number'])] = (str(row['number']), row['area'], row['province'], row['city'], row['county'])
    return official


def fix2():
    df = read("户籍(老)-处理结果2.xlsx", sheet_name="官方")
    no_province = df.loc[pandas.isna(df['province'])]
    office_dic = get_office_dic()
    for index, row in no_province.iterrows():
        number = str(row['number'])
        if not number.endswith('0000'):
            number0000 = number[0:2] + '0000'
            if number0000 in office_dic and office_dic[number0000][2] in row['area']:
                # print(number, row['area'], office_dic[number0000][2])
                province = office_dic[number0000][2]
                if number.startswith("11") or number.startswith("12") \
                        or number.startswith("50") or number.startswith("31"):
                    city = province
                    county = row['area'].replace(province, "")
                else:
                    city = row['area'].replace(province, "")
                    if "市" in city:
                        split_ = city.split("市")
                        city = split_[0] + "市"
                        county = split_[1]
                    elif "地区" in city:
                        split_ = city.split("地区")
                        city = split_[0] + "地区"
                        county = split_[1]
                    elif "地区" in city:
                        split_ = city.split("地区")
                        city = split_[0] + "地区"
                        county = split_[1]
            print(index, number, row['area'], province, city, county)
            df.loc[index, 'province'] = province
            df.loc[index, 'city'] = city
            df.loc[index, 'county'] = county
    with pandas.ExcelWriter("户籍(老)-处理结果3.xlsx") as writer:
        df.to_excel(writer, sheet_name='官方', index=False)


def fix3():
    df = read("户籍(老)-处理结果4.xlsx", sheet_name="官方")
    # no_province = df.loc[pandas.isna(df['province'])]
    # office_dic = get_office_dic()
    # print(no_province)
    for index, row in df.iterrows():
        number = str(row['number'])
        if str(row['province']) in str(row['county']):
            # county = row['county'].replace(row['province'])
            print(number, row['area'], row['province'], row['city'], row['county'])
            # df.loc[index, 'county'] = row['county'].replace(row['province'], "")

    # with pandas.ExcelWriter("户籍(老)-处理结果4.xlsx") as writer:
    #     df.to_excel(writer, sheet_name='官方', index=False)

if __name__ == '__main__':
    # fix()
    # sort_by_number()
    # fix2()
    fix3()
    pass
