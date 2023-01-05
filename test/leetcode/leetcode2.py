#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 15:01
# @Author  : ZhangL
import os
import re
import shutil

import convert_encoding_util as util

cwd = os.getcwd()
source = "C:\\Project\\算法\\leetcode\源文件\\"
java = cwd + "\\src\\run\\java2\\"


def run():
    # java_count = 0
    for parent, dirs, files in os.walk(source):
        for file in files:
            if ".java" in file:
                package = parent.split("\\")[-2]
                num = package.split("][")[0][1:5]
                title = package.split("][")[1][0:-1]
                class_name_final = file

                # 创建包
                package_name = "lt" + num
                import_package = "package %s;" % package_name
                package_path = java + package_name
                mkdir(package_path)

                # 添加package-info.java
                add_package_info(package, package_name, package_path)

                #  复制类
                class_final = package_path + "\\" + class_name_final
                shutil.copyfile(os.path.join(parent, file), class_final)

                # 添加package, todo 取消修改类名
                fix_class(class_final, import_package)


def add_package_info(package, package_name, package_path):
    package_info_path = package_path + "\\package-info.java"
    if not os.path.exists(package_info_path):
        shutil.copyfile("package-info.java", package_info_path)
        with open(package_info_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            content = content.replace("parent", package).replace("package_name", package_name)
            f.seek(0, 0)
            f.write(content)


def fix_class(file, package):
    with open(file, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(package + "\n" + content)


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    # print(re.sub("[a-z]","","SecondMinimumNodeInaBinaryTree"))
    run()

    pass
