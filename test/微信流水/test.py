#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/22
import pandas

left = pandas.DataFrame({'姓名': ['张三', '李四', '王五', '赵六'],
                         '年龄': ['19', '19', '20', '`4200000898202103090082469328']})

right = pandas.DataFrame({'姓名': ['孙七', '周八', '谢九', '刘十'],
                          '周岁': ['20', '23', '24', '25']})

print(left['年龄'].str.replace('`',''))
print(left['年龄'].str.replace('`',''))
print(left)

# print(left)
# print("=============================")
# print(right)
# print("=============================")
#
# left_duplicated = left.drop_duplicates(['年龄'])
# right_duplicated = right.drop_duplicates(['周岁'])
# result = pandas.merge(left_duplicated, right_duplicated,
#                       how='outer', left_on='年龄', right_on="周岁", indicator=True)
# print(result)
#
# result.loc[result['_merge'] == 'left_only'].to_excel("left-only.xlsx", index=False)
# result.loc[result['_merge'] == 'right_only'].to_excel("right-only.xlsx", index=False)

# print("`QTRAHB2021053115045500007502".__len__())
# print("`申请退款总金额".__len__())
