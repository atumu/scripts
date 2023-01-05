#!/bin python
# -*- coding: utf-8 -*-

import os
from datetime import datetime

import exifread


def get_file_time(filepath, timeformat):
    FIELD = 'EXIF DateTimeOriginal'
    fd = open(filepath, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    if FIELD in tags:
        # print(tags[FIELD]) --> 2021:08:26 06:04:14
        if "-" in timeformat:
            file_time = str(tags[FIELD]).replace(":", "-")
        else:
            file_time = str(tags[FIELD]).replace(":", "").replace(" ", "")
    else:
        file_time = datetime.fromtimestamp(os.path.getctime(filepath)).strftime(timeformat)
    # print(file_time)
    return file_time


def sort_by_second(elem):
    return elem[1]


def rename_to_time(dir, list):
    for item in list:
        # print(item[1], item[0].split(".")[0], item[1] == item[0].split(".")[0])
        # if item[1] == item[0].split(".")[0]:
        #     continue
        old = os.path.join(dir, item[0])

        extension = os.path.splitext(old)[1]
        new = os.path.join(dir, item[1] + extension)
        # avoid duplicate files
        step = 1
        while os.path.exists(new):
            new = os.path.join(dir, item[1] + " " + str(step) + extension)
            step += 1
        print(old, " --> ", new)
        os.rename(old, new)


if __name__ == '__main__':
    # time_format = "%Y-%m-%d %H-%M-%S"
    time_format = "%Y%m%d%H%M%S"

    dir = "C:\\Users\\zl409\\Desktop\\小板"

    list = []
    for filename in os.listdir(dir):
        filepath = os.path.join(os.path.abspath(dir), filename)
        if os.path.isfile(filepath):
        # if os.path.isfile(filepath) and filename.endswith('.jpg'):
            list.append((filename, get_file_time(filepath, time_format)))
    # print(list)
    rename_to_time(dir, list)
