#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 13:55
# @Author  : ZhangL

import difflib
import re


def ratio(str1, str2):
    seq = difflib.SequenceMatcher(lambda x: x == ' ', str1, str2)
    return seq.ratio()


def clear(target: str):
    s1 = re.sub('[\u4e00-\u9fa5]*', "", target)  # 剔除 中文
    s2 = re.sub('\([\d]{4}\)', "", s1)  # 剔除 (年份)
    s3 = s2.strip()  # 删除空格
    return s3


def ratio_top(target: str, arr: list):
    target = target.strip()
    similar = ''
    max_ratio = 0
    for s in arr:
        r = ratio(target, clear(s))
        if r > max_ratio:
            max_ratio = r
            similar = s
    if max_ratio < 0.9:
        return 0, ''
    else:
        return max_ratio, similar


if __name__ == '__main__':
    str1 = "Hello, I'm Your Aunt!"
    str2 = "Hello - I'm Your Aunt!"

    # str1 = "Steal Big Steal Little"
    # str2 = "Steal Big, Steal Little"
    # print(ratio(str1, str2))

    # str1 = "Steal Big Steal Little"
    # arr = ['惊逢敌手 Steal Big, Steal Little (1995)', '国际巨窃案 The Big Steal (1949)', '偷龙转凤 How to Steal a Million (1966)',
    #        '大小谎言 第一季 Big Little Lies Season 1 (2017)', '大小谎言 第二季 Big Little Lies Season 2 (2019)']

    str1 = "My Favorite Season"
    arr = ['火星叔叔马丁 第一季 My Favorite Martian Season 1 (1963)', '我最爱的战争 My Favorite War (2020)', '外星人报到 My Favorite Martian (1999)', '金色年代 My Favorite Year (1982)', '我最喜爱的物什 My Favorite Things (2009)']
    print(ratio_top(str1, arr))
