#!/bin python
# -*- coding: utf-8 -*-

import os

import pandas as pd


# 读取单个excel
def read(root, name):
    date = name[0:8]  # 根据文件名, 提取日期
    yxhb_sum = 0  # 当前日期内,圆心惠宝参保人数
    no_yxhb_sum = 0  # 当前日期内,非圆心惠宝参保人数

    excel_file = os.path.join(root, name)  # excel文件地址
    excel_df = pd.read_excel(excel_file)  # pandas读取excel生成DataFrame文件(标题自动转为列名, 真正数据行不包括标题)

    for index, row in excel_df.iterrows():  # 遍历每行数据,index为行号, row为一行数据
        code = str(row['渠道编码'])  # 读取当前行的编码
        num = int(row['参保人数'])  # 读取当前行的参保人数
        if code.startswith('yxhb'):  # 判断编码是否以'yxhb'开头
            yxhb_sum += num  # 等于: yxhb_sum = yxhb_sum + num
        else:
            no_yxhb_sum += num  # 等于: no_yxhb_sum = no_yxhb_sum + num

    return [date, yxhb_sum, no_yxhb_sum]  # 返回一个列表: ['日期', '圆心惠宝参保人数','非圆心惠宝参保人数']


# 保存统计结果到excel
def write(datas, target):
    # 三个标题
    date_title = '日期'
    yxhb_title = 'yxhb_参保人数'
    no_yxhb_title = '非yxhb_参保人数'

    # 新建一个DataFrame数据对象, 用来保存统计结果
    # 结果类似:
    #    日期   | yxhb_参保人数 | 非yxhb_参保人数
    # 20210508 |     5378     |    9317
    # 20210509 |     4621     |    9624
    result = pd.DataFrame(datas, columns=[date_title, yxhb_title, no_yxhb_title])

    yxhb_sum_total = result[yxhb_title].sum()  # 对所有日期的圆心惠宝参保人数进行求和
    no_yxhb_sum_total = result[no_yxhb_title].sum()  # 对所有日期的非圆心惠宝参保人数进行求和

    # 在最后一行之后新增加一行汇总数据
    result = result.append({date_title: "汇总", yxhb_title: yxhb_sum_total, no_yxhb_title: no_yxhb_sum_total},
                           ignore_index=True)

    # print(result)
    # 日期  yxhb_参保人数  非yxhb_参保人数
    # 0  20210508       5378        9317
    # 1  20210509       4621        9624
    # 2       汇总       9999       18941

    # 保存最终结果到excel
    result.to_excel(target, index=False)


if __name__ == '__main__':
    path = "渠道统计数据2"  # 数据地址
    target = "结果.xlsx"  # 保存统计结果的文件名

    datas = []  # 数据列表

    for root, dirs, files in os.walk(path, topdown=False):  # 遍历数据地址
        for name in files:  # 挨个处理文件
            datas.append(read(root, name))  # 合并读取结果
    print(datas)  # 结果模板: [['20210508', 5378, 9317], ['20210509', 4621, 9624]...]
    write(datas, target)  # 保存结果
