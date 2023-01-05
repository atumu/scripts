import os
import re
import sys
import time

import requests as requests

headers = {
    'Host': 's.taobao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'cookie': "t=368d939557465c2054b391ffa63deb0c; cookie2=19c74fbca88e7c876a6d95bbca30087d; v=0; cna=oRtnGAz2I14CAW/F+Frv+76+; _samesite_flag_=true; dnk=\u5F20\u541B\u6728\u6728; tracknick=\u5F20\u541B\u6728\u6728; enc=c0mk7pP39LwR7aRenRkCuo7vHJKqX6aSFrljiXgJ+kvFOCll/bZtyhUOGCEy2dtrnNy7RVShLS55V0k/MUOUag==; hng=CN|zh-CN|CNY|156; thw=cn; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; miid=496146292117005714; _tb_token_=7384d74e7a77f; ctoken=KReTzOC2wHG90prkE23Arhllor; sgcookie=E1004ZZMS0AfnNf56YFAFRy7a9ZA774oHRsC+cwnQzWwrmeDWYNhsbolyWGbwGl/wxJPx4gszpVqDvcqus0kI6VL7g==; csg=83b5bae4; skt=236bcee53e288200; existShop=MTYyMTA2ODE3MA==; _cc_=VFC/uZ9ajQ==; uc1=cookie16=UtASsssmPlP/f1IHDsDaPRu+Pw==&existShop=false&cookie21=U+GCWk/7p4mBoUyS4E9C&pas=0&cookie14=Uoe2zshtc6AoYw==; _m_h5_tk=1e3ed61eea3ecde0cfef8451af636739_1624168353613; _m_h5_tk_enc=11a4a63684a81cc2c389d0c236ffbc73; mt=ci=-1_1; _uab_collina=162426281453965691416774; x5sec=7b227365617263686170703b32223a22643136353465356164343939356336373761326566636639313230373865646143496578776f5947454c7a346e342f712b35765276514561437a63324f546b314d6a45774f4473784d4b6546677037382f2f2f2f2f77453d227d; JSESSIONID=8A8C1404285E1C66FF02754CBD38BD5F; tfstk=cmKPBj17V0nzNQSIWgsUdwfxHnsRZXKMvmWNrET_h1JulTQliMNdn03J3p5tmaf..; l=eBO6KKIIO6ZNkapSBOfwourza77OSIRAguPzaNbMiOCPO7fp5PA5W69Y6jT9C3GVh6qwR3yf4eUwBeYBqIv4n5U62j-la_kmn; isg=BG5utIibgonsL8maXlBodSnBv8QwbzJpaMQ9FJg32nEsew7VAP-CeRR5M-eXoyqB"
        .encode('utf-8').decode('latin-1'),
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'upgrade-insecure-requests': '1',
    'referer': 'https://s.taobao.com/',
}


def get_data(url):
    # 请求网页内容
    #         url = "https://s.taobao.com/search?q=螺蛳粉&ie=utf8&bcoffset=0&ntoffset=0&s=0"
    ###requests+请求头headers
    r = requests.get(url, headers=headers)
    r.encoding = 'utf8'
    s = (r.content)
    ###乱码问题
    html = s.decode('utf8')

    # 获取到网页中的javascritp数据中，接着通过正则表达式去提前所需内容（标题、销售地、销售量、评论数、销售价格、商品惟一ID、图片URL）
    # 正则模式
    p_title = '"raw_title":"(.*?)"'  # 标题
    p_location = '"item_loc":"(.*?)"'  # 销售地
    p_sale = '"view_sales":"(.*?)人付款"'  # 销售量
    p_comment = '"comment_count":"(.*?)"'  # 评论数
    p_price = '"view_price":"(.*?)"'  # 销售价格
    p_nid = '"nid":"(.*?)"'  # 商品惟一ID
    p_img = '"pic_url":"(.*?)"'  # 图片URL

    # 正则解析
    title = re.findall(p_title, html)
    location = re.findall(p_location, html)

    sale = re.findall(p_sale, html)
    comment = re.findall(p_comment, html)
    price = re.findall(p_price, html)
    nid = re.findall(p_nid, html)
    img = re.findall(p_img, html)

    # 将正则表达式提取的数据放入到集合data中（方便后面统一保存到csv）
    # 数据集合
    data = []
    for j in range(len(title)):
        data.append([title[j], location[j], sale[j], comment[j], price[j], nid[j], "https:" + img[j]])

    if len(data) == 0:
        print(html)
    return data


# 保存数据到csv
# 导入python操作csv相关库
import xlrd
import xlwt
from xlutils.copy import copy


# 追加写入excel
def write_excel_xls_append(path, value):
    # print("write_excel_xls_append方法执行")
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿


# 填充数据
def write_excel(book_name_xls, data):
    if not os.path.exists(book_name_xls):
        # 创建一个workbook，设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet

        worksheet = workbook.add_sheet('淘宝-螺蛳粉')
        workbook.save(book_name_xls)
        # 写入表头
        value1 = [["标题", "销售地", "销售量", "评论数", "销售价格", "商品惟一ID", "图片URL"]]
        write_excel_xls_append(book_name_xls, value1)

    # 开始保存
    # 通过追加的方式可以将螺蛳粉商品数据保存到excel中！
    # 淘宝上的『螺蛳粉』商品一共是100页（每页44条，共100*44条数据）
    write_excel_xls_append(book_name_xls, data)
    time.sleep(3)  # 为了防止禁ip，设置每一页的爬取时间间隔为3秒


if __name__ == '__main__':
    book_name_xls = '螺蛳粉.xls'
    if os.path.exists(book_name_xls):
        os.remove(book_name_xls)

    for i in range(0, 4):
    # for i in range(0, 101):
        url = "https://s.taobao.com/search?q=螺蛳粉&ie=utf8&bcoffset=0&ntoffset=0&s=" + str(i * 44)

        print(url)
        data = get_data(url)

        if len(data) == 0:
            print("获取数据为空, 建议优先替换cookie")
            sys.exit()

        print(len(data))
        write_excel(book_name_xls, data)
