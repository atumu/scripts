#!/usr/bin/python
# encoding: utf-8

"""
@version: 0.0.1
@author: zhangl
@time: 2016/8/17 18:05
"""

import datetime
import time

import MySQLdb
import tablib

host = '127.0.0.1'
user = 'root'
passwd = 'zhangL'
db_name = 'test'  # TODO 目标数据库
table_name = 'student'  # TODO 目标表


# 导出表数据到excel(字段注释作标题)
def export_data_to_excel():
    schema = Info_schema()
    # excel 文件名
    excel_name = schema.get_table_name()

    # excel 列标题
    excel_heads = schema.get_column_comments()
    # print json.dumps(excel_heads,ensure_ascii=False)

    # 数据
    db = DB()
    data = []
    data = db.get_table_data()

    data = tablib.Dataset(*data, headers=excel_heads)
    # print data.csv
    with open(excel_name + '.xls', 'wb') as f:
        f.write(data.xls)


# 从库information_schema查询表结构
class Info_schema():
    def __init__(self):
        self.con = MySQLdb.connect(user=user, passwd=passwd, host=host, db='information_schema', charset='utf8')
        self.cursor = self.con.cursor()

    # 查询表注释
    def get_table_name(self):
        sql_query_comment = """SELECT
                                  table_comment
                                FROM
                                TABLES
                                WHERE
                                table_schema = '%s'
                                AND table_name = '%s'
                                GROUP BY
                                table_name;
                                """ % (db_name, table_name)
        self.cursor.execute(sql_query_comment)
        table_info = self.cursor.fetchone()
        return table_info[0]

    # 查询字段注释
    def get_column_comments(self):
        sql_query_columns = """SELECT
                                    column_name,
                                    column_comment,
                                    column_type
                                FROM
                                    COLUMNS
                                WHERE
                                    table_schema = '%s'
                                AND table_name = '%s';
                                """ % (db_name, table_name)
        self.cursor.execute(sql_query_columns)
        column_comments = []
        for column in self.cursor.fetchall():
            head = column[0] if column[1] == "" else column[1]
            column_comments.append(head)
        return column_comments


# 查询表数据
class DB():
    def __init__(self):
        self.con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db_name, charset='utf8')
        self.cursor = self.con.cursor()

    def get_table_data(self):
        sql_get_table_data = """SELECT * FROM %s;""" % table_name
        self.cursor.execute(sql_get_table_data)
        data = self.cursor.fetchall()

        # 将date型字段置换为字符串, 防止tablib输出到excel时日期字段报错
        if len(data) > 0:
            t_list = []
            date_indexs = []
            for i, col in enumerate(data[0]):
                if type(col) in (datetime.datetime, time.time):
                    date_indexs.append(i)

            if len(date_indexs) > 0:
                for i, row in enumerate(data):
                    l = list(row)
                    for index in date_indexs:
                        l[index] = unicode(l[index])
                    t_list.append(tuple(l))
            return tuple(t_list)


if __name__ == '__main__':
    export_data_to_excel()
