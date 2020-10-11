#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 18:54
# @Author  : ZhangL

import json

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
print(js)

json_str \
    = """{
    "a":1,
    "b":2,
    "c":3
}"""

l = json.loads(json_str)
print(l)
