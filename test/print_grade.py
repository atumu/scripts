#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/9
# @Author  : zhangl
import random


def grade():
    return random.randint(60, 100)


def subject():
    subjects = ['精算学', '社保学', '保险学']
    return subjects[random.randint(0, 2)]


for i in range(1000):
    print(("%d\t%d\t%d\t%d\t%d\t%d\t%s") % (grade(), grade(), grade(), grade(), grade(), grade(), subject()))
