#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18


from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
import os

excel_path = 'data_大区版.xlsx'
locate_title = '地区'
target_title = '目标任务'
run_title = '冲刺目标'

excel_dataframe = pd.read_excel(excel_path)
locate = excel_dataframe[locate_title].to_list()
already_values = excel_dataframe[target_title].to_list()
million_values = excel_dataframe[run_title].to_list()

price_list = [[locate[i], already_values[i], million_values[i]] for i in range(len(locate))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="2021-圆心惠宝"),
    visualmap_opts=opts.VisualMapOpts(min_=0, max_=1)  # 最大数据范围
)
map_1.add("2021-圆心惠宝", price_list, maptype="china")
map_1.render("yuanxin.html")

os.system("yuanxin.html")
