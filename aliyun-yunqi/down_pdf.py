#!/usr/bin/python
# encoding: utf-8


"""
@version: ??
@author: zhangl
@contact: zhanglin@miduo.com
@site: https://www.miduo.com
@time: 2017/3/16 15:30
"""
import json
import os
import sys

import io
import requests
from lxml import html

sys.setdefaultencoding('utf-8')

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


# 获取文件链接
def get_links():
    response = requests.get('https://yq.aliyun.com/articles/69316')
    tree = html.fromstring(response.text)
    xpaths = [{"date": "3月8日更新", "xpath": "/html/body//div[@class='content-detail']/p[7]/a"},
              {"date": "3月2日更新", "xpath": "/html/body//div[@class='content-detail']/p[8]/a"},
              {"date": "2月24日更新", "xpath": "/html/body//div[@class='content-detail']/p[9]/a"},
              {"date": "2月22日更新", "xpath": "/html/body//div[@class='content-detail']/p[10]/a"},
              {"date": "2月20日更新", "xpath": "/html/body//div[@class='content-detail']/p[11]/a"},
              {"date": "2月14日更新", "xpath": "/html/body//div[@class='content-detail']/p[12]/a"},
              {"date": "2月10日更新", "xpath": "/html/body//div[@class='content-detail']/p[13]/a"}]

    link_list = []
    for xpath in xpaths:
        date = xpath['date']
        path = xpath['xpath']
        pdfs = []
        links = {"date": date, "pdfs": pdfs}
        aList = tree.xpath(path)
        for a in aList:
            pdfs.append({"name": a.text, "url": a.attrib['href']})
        link_list.append(links)
    # print json.dumps(link_list)
    return link_list


# 下载pdf
def down_pdf(linkList):
    for links in linkList:
        print ("------------------------")
        print(links['date'])
        date_dir = 'data/' + links['date'].encode("gb2312") + '/'
        creat_dir(date_dir)
        count = 0
        for pdf in links['pdfs']:
            count += 1
            try:
                data = requests.get(pdf['url'], headers=headers, stream=True, timeout=30)
                print(data.content)
                # file = open(date_dir + count + ".pdf", 'wb+')
                # file.write(data.content)
                # file.close()
            except:
                print(pdf['name'])
                print(pdf['url'])


# 创建目录/文件
def creat_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


if __name__ == '__main__':
    links = get_links()
    # 失败啦
    # down_pdf(links)

    aliyun_pdf = {"title": "", "links": links}
    # with open('data/pdf.txt', 'w') as outfile:
    #     json.dump(aliyun_pdf, outfile)

    with io.open('data/pdf.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(aliyun_pdf, ensure_ascii=False))

    pass
