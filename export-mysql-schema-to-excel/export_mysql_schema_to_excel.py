# encoding: utf-8
"""
@version: 1.0
@author:  Atumu
@site: http://gongchangmumu.com
@software: PyCharm
@file: export_mysql_schema_to_excel.py
@time: 2016/4/4 16:42
"""

import pymysql
import xlsxwriter

user = 'root'  # your username
passwd = 'zhangL'  # your password
host = '127.0.0.1'  # your host
db = 'test'  # database where your table is stored
tables = ()  # table you want to save

# host = raw_input('请输入host:')  # your host
# user = raw_input('请输入用户名:')  # your username
# passwd = raw_input('请输入密码:')  # your password
# db = raw_input('请输入目标数据库:')  # database where your table is stored
# tables_require = raw_input('是否指定表(y/n)?')
# if tables_require == 'y':
#     tables = (raw_input('请输入目标表名:'))  # table you want to save

excelFile = "%s.xlsx" % db;
workbook = xlsxwriter.Workbook(excelFile)
sheet = workbook.add_worksheet();

format_table_name = workbook.add_format({'bold': True, 'font_color': 'red'})
format_headings = workbook.add_format({'bold': True, 'align': 'center ', 'valign': 'vcenter', 'fg_color': '#D7E4BC', 'border': 1})

sheet.freeze_panes(1, 0)
column_headings = (u'名', u'主键', u'类型', u'长度', u'允许null', u'默认值', u'注释')
sheet.write_row(0, 0, column_headings, format_headings)

con = pymysql.connect(user=user, passwd=passwd, host=host, db='information_schema', charset='utf8')
cursor = con.cursor()

query_db = "select table_name,table_comment from tables where table_schema = '%s' group by table_name;" % db
cursor.execute(query_db)
line_num = 1
for t in enumerate(cursor.fetchall()):
    if tables:
        if t[1][0] not in tables:
            continue
    sheet.write_row(line_num, 0, t[1], format_table_name)
    query_table = "select column_name,column_key,data_type,character_maximum_length,is_nullable,column_default,column_comment from columns where  table_schema = '%s' and table_name = '%s';" % (db, t[1][0])
    cursor.execute(query_table)
    columns = cursor.fetchall()
    for column in enumerate(columns):
        line_num = line_num + 1
        sheet.write_row(line_num, 0, column[1])
    line_num = line_num + 3

workbook.close()
