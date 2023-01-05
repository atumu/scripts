#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 16:50
# @Author  : ZhangL


import codecs
import os

import chardet

convertdir = "C:\\Project\\算法\\leetcode\源文件\\"

convertfiletypes = [
    ".java",
    ".h",
    ".hpp"
]


def convert_encoding(filename, target_encoding):
    # Backup the origin file.
    # convert file from the source encoding to target encoding
    content = codecs.open(filename, 'rb').read()
    source_encoding = chardet.detect(content)['encoding']
    if source_encoding != 'utf-8':
        print(source_encoding, filename)
        content = content.decode(source_encoding, 'ignore')  # .encode(source_encoding)
        codecs.open(filename, 'w', encoding=target_encoding).write(content)


def main():
    for root, dirs, files in os.walk(convertdir):
        for f in files:
            for filetype in convertfiletypes:
                if f.lower().endswith(filetype):
                    filename = os.path.join(root, f)
                    try:
                        convert_encoding(filename, 'utf-8')
                    except Exception as e:
                        print(filename, e)


if __name__ == '__main__':
    main()
