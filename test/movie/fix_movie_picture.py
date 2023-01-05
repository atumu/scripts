#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 11:30
# @Author  : ZhangL
import json
import time

import mysql.connector
import requests
import multiprocessing

mydb = mysql.connector.connect(
    host="192.168.3.88",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="zhangL",  # 数据库密码
    database='movie'
)
mycursor = mydb.cursor()


# mydb.autocommit = False


def get_movie_ids(start, offset):
    mycursor.execute("select movieid,version from movie limit %d,%d" % (start, offset))
    myresult = mycursor.fetchall()
    ids = []
    for result in myresult:
        if result[1] == 0:
            ids.append(result[0])
    return ids


def fill_pictures(ids):
    cookies = {}  # 初始化cookies字典变量
    headers = {
        'Connection': 'keep-alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    f = open(r'cookies.txt', 'r')  # 打开所保存的cookies内容文件

    for line in f.read().split(';'):  # 按照字符：进行划分读取
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内
    # requests
    for id in ids:
        try:
            resp = requests.get("https://movielens.org/api/movies/%s" % id, cookies=cookies, headers=headers, timeout=2)
            json_obj = json.loads(resp.text)

            if json_obj['status'] == 'fail':
                continue

            movie = json_obj['data']['movieDetails']['movie']
            picture = ''
            backpost = ''
            backposts = []

            posterPath = movie['posterPath']
            if posterPath is not None and len(posterPath) > 10:
                picture = "https://image.tmdb.org/t/p/original/%s" % movie['posterPath']

            backdropPaths = movie['backdropPaths']
            for b in backdropPaths:
                backposts.append("https://image.tmdb.org/t/p/original/%s" % b)
            if len(backposts) > 0:
                backpost = backposts[0]

            sql = "update movie set picture = '%s', backpost='%s',backposts = '%s',version = 1 where movieid = %s and version = 0" % (
                picture, backpost, ','.join(backposts), id)
            print("OK: %s" % id)
            # print(sql)
            mycursor.execute(sql)
            mydb.commit()
            time.sleep(0.1)
        except Exception as e:
            print(e)
            print("ERROR: %s" % id)
            print("===================")


if __name__ == '__main__':
    # print(get_movie_ids(0, 10))
    cpu_count = multiprocessing.cpu_count()
    length = 50581
    offset = 1000
    pool = multiprocessing.Pool(cpu_count)
    ids_list = []

    for start in range(0, length, offset):
        ids_list.append(get_movie_ids(start, offset))

    pool.map(fill_pictures, ids_list)
    pool.close()
    pool.join()
    print("完成")
