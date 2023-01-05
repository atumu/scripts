#!/usr/bin/python
# encoding: utf-8


"""
@version: ?
@time: 2017/7/12 15:19
"""

import requests
from lxml import html


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':

    names = [u"苏黎世中国", u"爱和谊日生同和(中国)", u"阳光财险重庆分公司", u"现代财产保险", u"安信农险", u"浙商保险", u"中华财险", u"长安责任险山东分公司", u"人保财险西藏分公司",
             u"人保财险河北分公司", u"长安责任险湖南分公司", u"阳光财险河南分公司", u"人保财险山西分公司", u"长安责任险福建分公司", u"平安健康险", u"阳光财险辽宁分公司",
             u"东京海上日动(中国)", u"人保财险山东分公司", u"人保财险江西分公司", u"长安责任险(浙江)", u"人保财险辽宁分公司", u"劳合社保险中国", u"中国人寿(海外)",
             u"人保财险湖北分公司", u"阳光农险", u"安邦保险集团", u"中煤保险", u"阳光财险宁波分公司", u"中国人保寿险", u"人保财险(陕西)", u"人保财险广东分公司", u"太平保险",
             u"中国人寿养老险公司", u"人保财险上海分公司", u"陆家嘴国泰人寿", u"中航安盟财险", u"阳光财险山东分公司", u"阳光财险云南分公司", u"人保财险青岛分公司", u"平安产险",
             u"阳光财险青海分公司", u"国元保险", u"人保财险贵州分公司", u"阳光财险四川分公司", u"人保财险安徽分公司", u"人保财险海南分公司", u"阳光财险江苏分公司", u"渤海保险",
             u"英大财险", u"阳光财险宁夏分公司", u"人保财险内蒙古分公司", u"人保财险江苏分公司", u"鼎和保险", u"中银三星人寿", u"鑫安保险公司", u"人保财险河南分公司", u"新华保险",
             u"交银康联", u"阳光财险北京分公司", u"太保产险", u"英大人寿", u"人保财险厦门分公司", u"人保财险湖南分公司", u"德华安顾人寿", u"都邦保险", u"阳光财险山西分公司",
             u"君康人寿", u"人保财险天津分公司", u"天安财险", u"人保财险青海分公司", u"人保财险吉林分公司", u"中国大地保险", u"人保财险云南分公司", u"人保财险大连分公司",
             u"人保财险重庆分公司", u"阳光财险上海分公司", u"人保财险浙江分公司", u"阳光财险新疆分公司", u"乐爱金产险", u"日本财险(中国)", u"人保财险甘肃分公司", u"人保财险黑龙江分公司",
             u"富德产险", u"长安责任险宁波支公司", u"人保财险广西分公司", u"安诚保险", u"三星财产(中国)", u"中美大都会人寿保险", u"阳光财险浙江分公司", u"人保财险四川分公司",
             u"锦泰保险", u"三井住友海上火灾险", u"阳光产险", u"人保财险宁波分公司", u"人保财险深圳分公司", u"永安保险公司", u"泰山保险", u"人保财险新疆分公司", u"阳光财险贵州分公司",
             u"太保寿险", u"华安保险", u"阳光财险天津分公司", u"诚泰保险", u"安盛中国", u"人保财险(福建)", u"中国财险", u"人保财险北京分公司", u"阳光财险广东分公司",
             u"华农保险", u"招商信诺", u"长安责任险江苏分公司", u"人保财险宁夏分公司"]

    URL = "http://insurance.jrj.com.cn/html/ic/list/ics-%s.shtml"
    aXpath = "//div[@class='cl1']//strong/a"
    start = 18
    end = 0
    for i in range(end, start):
        url = URL % i
        tree = html.fromstring(requests.get(url).text)
        _as = tree.xpath(aXpath)
        for a in _as:
            text = a.text.strip()
            for name in names:
                if text == name:
                    print( text + "\t", "http://insurance.jrj.com.cn" + a.get('href') + "\t")

    _url = "http://insurance.jrj.com.cn/html/ic/list/ics.shtml"
    tree = html.fromstring(requests.get(_url).text)
    _as = tree.xpath(aXpath)
    for a in _as:
        text = a.text.strip()
        for name in names:
            if text == name:
                print (text + "\t", "http://insurance.jrj.com.cn" + a.get('href') + "\t")
