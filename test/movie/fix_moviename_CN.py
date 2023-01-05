#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 10:02
# @Author  : ZhangL
from __future__ import unicode_literals
import re

import pymysql

db = pymysql.connect('192.168.3.88', 'root', 'zhangL', 'movie')
cursor = db.cursor()


def update_sql(sql):
    # level = 'dev'
    level = 'pro'
    if level == 'dev':
        print(sql)
    elif level == 'pro':
        cursor.execute(sql)
        db.commit()


def fix():
    # sql = "select movieid, version, moviename, moviename_CN from movie2 where version = 1 and moviename_CN is not null and movieid = 105359"
    # sql = "select movieid, version, moviename, moviename_CN from movie2 where version = 1 and moviename_CN is not null and movieid = 105366"
    # sql = "select movieid, version, moviename, moviename_CN from movie2 where version = 1 and moviename_CN is not null and movieid = 105377"
    sql = "select movieid, version, moviename, moviename_CN from movie2 where version = 1 and moviename_CN is not null and movieid = 63121"
    # sql = "select movieid, version, moviename, moviename_CN from movie2 where version = 1 and moviename_CN is not null"
    cursor.execute(sql)
    results = cursor.fetchall()

    print(len(results))
    count = 0

    for result in results:
        movieid = result[0]
        moviename = result[2]
        moviename_CN: str = result[3]
        try:
            cns = re.findall('u[4e00-9fa5]{4}', moviename_CN)

            if len(cns) > 0:
                print(movieid, moviename, moviename_CN)
                count = count + 1
                moviename_cn_split = moviename_CN.split(" ")
                fuck = moviename_cn_split[0]
                fuck_ok = ' '.join(moviename_cn_split[1:])
                fuck_new = ''
                for f in fuck:
                    if f == 'u':
                        fuck_new = fuck_new + "\\";
                    fuck_new = fuck_new + f;
                cn_name = fuck_new.encode("utf-8").decode('unicode_escape')

                new_moviename_CN = cn_name + " " + fuck_ok
                print(movieid, moviename, new_moviename_CN)
                sql = "update movie2 set moviename_CN = '%s' where movieid = %s" \
                      % (pymysql.escape_string(new_moviename_CN), movieid)
                print(sql)
                cursor.execute(sql)
                print("=================================")
        except UnicodeDecodeError as e:
            print(movieid, moviename, moviename_CN)
            print("=================================")

    print(count)


def debug():
    s = 'u53ccu57ceu8bb0'
    print(re.findall('u[4e00-9fa5]{4}', s))
    print(re.sub('[u4e00-u9fa5]*', "|", s))
    pass


if __name__ == '__main__':
    debug()
    # fix()
    # db.commit()
    # db.close()
    # s = 'u52c7u6c14u4e4bu7ffc Wings of Courage (1995)'
    # print()
