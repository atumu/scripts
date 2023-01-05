# encoding: utf-8
"""
@version: 0.0.1
@author:  Atumu
@software: PyCharm
@file: check_key_from_dir.py
@time: 2016/4/5 14:44

# 判断文件中是否包含关键字,将文件路径打印出来
"""
import os
import sys


# 返回指定目录的所有文件（包含子目录的文件）
def get_all_file(floder_path):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            file_list.append(dirpath + os.sep + name)
    return file_list


# 搜索
def is_file_contain_word(file_list, extension, word):
    for _file in file_list:
        if extension.strip() == '' or os.path.splitext(_file)[-1][1:] == extension:
            try:
                if word.lower() in open(_file, errors="ignore", encoding="utf-8").read().lower():
                    print(_file)
            except:
                print("文件 ", _file, " 出错: ", sys.exc_info()[0])
    print("\n完成搜索.")


def from_input():
    query_word = input("请输入要查询的内容:\n")

    while query_word.strip() == '':
        query_word = input("必须输入要查询的内容:\n")

    query_extension = input("请输入文件后缀(不指定->直接回车):\n")
    basedir = input("请输入目标文件夹地址(当前目录->直接回车):\n")

    if basedir.strip() == '':
        # 指定当前目录为目标文件夹
        basedir = os.getcwd()

    if query_extension.strip() == '':
        print("开始在 %s 下搜索 %s ...\n\n" % (basedir, query_word))
    else:
        print("开始在 %s 的 .%s 中搜索 %s ...\n\n" % (basedir, query_extension, query_word))

    is_file_contain_word(get_all_file(basedir), query_extension, query_word)


if __name__ == '__main__':
    # from_input()
    basedir = "C:\Project"
    query_extension = "java"
    query_word = "WatchDog"
    is_file_contain_word(get_all_file(basedir), query_extension, query_word)
