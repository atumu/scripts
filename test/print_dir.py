#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 9:15
# @Author  : ZhangL

import os
import os.path
import re


def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")
    paths = os.listdir(path)
    paths.sort(key=lambda x: int(re.findall("\d+", x)[0]) if re.findall("\d+", x) else 0)

    for item in paths:
        if 'print_dir.py' not in item and item.split('.')[-1] not in ['class']:
            print("  " * depth + " " + item)
            newitem = path + '/' + item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth + 1)


if __name__ == '__main__':
    dfs_showdir('D:\公务员\公务员', 0)
