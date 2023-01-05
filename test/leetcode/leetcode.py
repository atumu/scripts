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
java = cwd + "\\src\\run\\java\\"


def run():
    # java_count = 0
    for parent, dirs, files in os.walk(source):
        # 当前目录下修改过的新旧类名
        class_map_false = False
        class_map = {}
        package_path = ''
        for file in files:
            if ".java" in file:
                class_map_false = True
                # java_count = java_count + 1
                package = parent.split("\\")[-2]
                num = package.split("][")[0][1:5]

                title = package.split("][")[1][0:-1]
                class_name_temp = title.replace(" ", "")
                if len(class_name_temp) > 12:
                    class_name_temp = re.sub("[a-z]", "", class_name_temp)

                old_name = file
                class_name_final = get_class_name_final_2(old_name, class_name_temp)
                # print(class_name_temp, old_name, class_name_final)
                class_map[old_name.split(".")[0]] = class_name_final

                # 创建包
                package_name = "lt" + num
                import_package = "package %s;" % package_name
                package_path = java + package_name
                mkdir(package_path)

                # 添加package-info.java
                add_package_info(package, package_name, package_path)

                # #  复制类
                # class_final = package_path + "\\" + class_name_final + ".java"
                # shutil.copyfile(os.path.join(parent, file), class_final)
                # # 修改编码
                # util.convert_encoding(class_final, "utf-8")
                # # 添加package, 修改类名
                # fix_class(class_final, class_name_final, import_package)
        # if class_map_false:
        if False:
            # class_map 的key 从长到短装进数组
            keys = list(class_map.keys())
            keys.sort()
            keys.reverse()
            for p, ds, fs in os.walk(package_path):
                for f in fs:
                    with open(os.path.join(p, f), 'r+', encoding='utf-8') as f:
                        content = f.read()
                        for key in keys:
                            re.sub()
                            content = content.replace(key, class_map[key])
                        f.seek(0, 0)
                        f.write(content)

            print("old: %s\nnew: %s\nclass: %s\n\n" % (parent, package_path, class_map))


def add_package_info(package, package_name, package_path):
    package_info_path = package_path + "\\package-info.java"
    if not os.path.exists(package_info_path):
        shutil.copyfile("package-info.java", package_info_path)
        with open(package_info_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            content = content.replace("parent", package).replace("package_name", package_name)
            f.seek(0, 0)
            f.write(content)


def fix_class(file, class_name_final, package):
    with open(file, 'r+', encoding='utf-8') as f:
        # print(class_name_final)
        content = f.read()
        content = re.sub("public class \w+ {", "public class " + class_name_final + " {", content)
        f.seek(0, 0)
        f.write(package + "\n" + content)


def get_class_name_final_2(old_name, class_name_temp):
    class_map = {'Main': 'Main%s',
                 'Solution': '%s',
                 'Solution1': '%s1',
                 'Solution2': '%s2',
                 'Solution3': '%s3',
                 'Test': 'Test%s',
                 'ListNode': 'ListNode%s',
                 'TreeNode': 'TreeNode%s',
                 'SolutionTest': 'Test%s',
                 'Node': 'Node%s'}
    for key in class_map.keys():
        if (key + ".java") == old_name:
            return class_map[key] % class_name_temp
    return old_name.split(".")[0]


def get_class_name_final(old_name, class_name_temp):
    if old_name == "Main.java":
        class_name_new = "Main%s.java" % class_name_temp
    elif old_name == "Solution.java":
        class_name_new = "%s.java" % class_name_temp
    elif old_name == "Solution1.java":
        class_name_new = "%s1.java" % class_name_temp
    elif old_name == "Solution2.java":
        class_name_new = "%s2.java" % class_name_temp
    elif old_name == "Solution3.java":
        class_name_new = "%s3.java" % class_name_temp
    elif old_name == "Test.java":
        class_name_new = "Test%s.java" % class_name_temp
    elif old_name == "ListNode.java":
        class_name_new = "%sListNode.java" % class_name_temp
    elif old_name == "TreeNode.java":
        class_name_new = "%sTreeNode.java" % class_name_temp
    elif old_name == "SolutionTest.java":
        class_name_new = "%sTest.java" % class_name_temp
    elif old_name == "Node.java":
        class_name_new = "%sNode.java" % class_name_temp
    else:
        class_name_new = old_name
    return class_name_new


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    # print(re.sub("[a-z]","","SecondMinimumNodeInaBinaryTree"))
    # run()

    pass
