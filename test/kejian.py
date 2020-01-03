#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 18:27
# @Author  : ZhangL

import os
import shutil

type = "1. 核心知识篇"
# type = "2. 高手进阶篇"

path = "D:\教程\Elasticsearch顶尖高手系列\\" + type
shipin_path = path + "\\视频\\"
kejian_path = path + "\\资料\\课件\\"

shipin_map = {}
kejian_map = {}

for dir in os.walk(shipin_path):
    file_list = dir[2]
    for shipin in file_list:
        shipin_arr = shipin.split(".", 1)
        shipin_map[shipin_arr[0]] = shipin_path + shipin
# print(shipin_arr)


for dir in os.listdir(kejian_path):
    kejian = kejian_path + dir
    if os.path.isdir(kejian):
        kejian_index = dir.split("：")[0].replace("第", "").replace("节", "")
        kejian_map[kejian_index] = kejian

# print(kejian_map)

for index in kejian_map.keys():
    kejian_dir = kejian_map[index]
    name = kejian_dir.split("\\")[6]
    dst = path + "\\" + name
    if os.path.exists(dst):
        shutil.rmtree(dst)

    shutil.copytree(kejian_dir, dst)
    os.remove(dst + "\\课程PPT.ppt")
    os.rename(dst + "\\课程笔记.txt", dst + "\\" + name + ".txt")


    # print(shipin_map[index])
    shutil.copy(shipin_map[index], dst)
