#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 22:08
# @Author  : ZhangL
import requests

result = requests.get('https://data.10jqka.com.cn/financial/yjyg/')
# result = requests.get('https://s.thsi.cn/css/datacenter/financial/page-202008032148.min.css')
print(result.text)