#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 13:59
# @Author  : ZhangL

# !/bin python
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
    sql = "select movieid, moviename,year(showyear), douban_movies from movie2 where version = -1 and douban_movies is not null"
    cursor.execute(sql)
    results = cursor.fetchall()

    print(len(results))
    count = 0

    for result in results:
        movieid = result[0]
        moviename = result[1]
        year = result[2]
        douban_movies: str = result[3]

        if "|||" not in douban_movies and str(year) in douban_movies:
            count = count + 1
            print(movieid, moviename, year, "==", douban_movies)
            sql = "update movie2 set moviename_CN = '%s',version = 1 where movieid = %s;" \
                  % (pymysql.escape_string(douban_movies), movieid)
            # print(sql)
            cursor.execute(sql)
        # print("=================================")

    print(count)


def debug():
    pass


if __name__ == '__main__':
    # debug()
    fix()
    db.commit()
    db.close()
