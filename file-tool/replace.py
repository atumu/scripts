#!\bin python
# -*- coding: utf-8 -*-
# @Time    : 2020\11\8 14:37
# @Author  : ZhangL

# 修复文件名

import os

target = "C:\\Users\\zl409\\Desktop\\葱头"
s = "微信图片_"

# re_compile = re.compile("第\d+章")
# old = os.path.join(root, d)
# new = re_compile.sub('',old)
# print(new)
# os.rename(old, new)

for root, dirs, files in os.walk(target):
    for d in dirs:
        if s in d:
            old = os.path.join(root, d)
            new = old.replace(s, "")
            os.rename(old, new)
    for f in files:
        if s in f:
            old = os.path.join(root, f)
            new = old.replace(s, "")
            os.rename(old, new)
