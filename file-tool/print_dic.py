#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26
# @Author  : zhangl

import os
import re

target = 'C:\\Users\\zl409\\Desktop\\77.编程必备基础 计算机组成原理+操作系统+计算机网络'

convert = lambda text: int(text) if text.isdigit() else text.lower()
alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]


def show_dir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")
    if '代码课件' not in path:
        listdir = os.listdir(path)
        listdir.sort(key=alphanum_key)
        for item in listdir:
            if '.git' not in item:
                print("| " * depth + "+--" + item)

                newitem = path + '/' + item
                if os.path.isdir(newitem):
                    show_dir(newitem, depth + 1)


if __name__ == '__main__':
    show_dir(target, 0)
