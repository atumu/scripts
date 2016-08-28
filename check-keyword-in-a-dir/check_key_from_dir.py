# encoding: utf-8
"""
@version: 0.0.1
@author:  Atumu
@software: PyCharm
@file: check_key_from_dir.py
@time: 2016/4/5 14:44
"""

import os

# 判断文件中是否包含关键字，是则将文件路径打印出来
def is_file_contain_word(file_list, query_word):
    for _file in file_list:
        if query_word in open(_file).read():
            print _file
    print("Finish searching.")


# 返回指定目录的所有文件（包含子目录的文件）
def get_all_file(floder_path):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            file_list.append(dirpath + '\\' + name)
    return file_list


query_word = raw_input("Please input the key word that you want to search:")
basedir = raw_input("Please input the directory:")

is_file_contain_word(get_all_file(basedir), query_word)


# raw_input("Press Enter to quit.")
