#!/bin python
# -*- coding: utf-8 -*-

import os


def rename_to_number(dir):
    file_list = os.listdir(dir)
    file_list.sort()
    print(file_list)
    index_list = file_list.copy()

    while len(file_list) != 0:
        filename = file_list.pop(0)

        number = index_list.index(filename) + 1

        old = os.path.join(os.path.abspath(dir), filename)
        extension = os.path.splitext(old)[1]

        new = os.path.join(os.path.abspath(dir), str(number) + extension)
        if os.path.exists(new):
            file_list.append(filename)
            continue
        else:
            print(old, " --> ", new)
            os.rename(old, new)


if __name__ == '__main__':
    dir = "C:\\Users\\zl409\\Desktop\\小板"
    rename_to_number(dir)
