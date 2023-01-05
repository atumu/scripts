#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/22
# @Author  : zhangl

import pandas

if __name__ == '__main__':
    df = pandas.read_excel("9.18_3-处理结果2.xlsx")
    sheng = df.groupby(['省','市']).count() #.sort_values(['count'], ascending=False)
    print(sheng)

    with pandas.ExcelWriter("9.18_3-处理结果2-统计.xlsx") as writer:
        sheng.to_excel(writer, sheet_name='结果', index=False)

