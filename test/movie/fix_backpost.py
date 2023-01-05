#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 14:53
# @Author  : ZhangL

import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.3.88",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="zhangL",  # 数据库密码
    database='movie'
)
mycursor = mydb.cursor()

# mydb.autocommit = False

# mycursor.execute("select count(1) from movie where version = 0")
# print(mycursor.fetchone()[0])

for offset in range(0, 50581, 1000):
    mycursor.execute("select movieid, backposts from movie limit %d,%d" % (offset, 1000))
    results = mycursor.fetchall()
    for result in results:
        id = result[0]
        backposts = result[1]
        if backposts is not None and "," in backposts:
            backpost = backposts.split(',')[0]
            sql = "update movie set backpost = '%s' where movieid=%s" % (backpost, id)
            mycursor.execute(sql)
    mydb.commit()
