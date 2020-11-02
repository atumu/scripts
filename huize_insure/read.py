#!/usr/bin/python
# encoding: utf-8


"""
@version: ??
@author: zhangl
@contact: zhanglin@miduo.com
@site: https://www.miduo.com
@time: 2016/10/18 10:24
"""
import json
import os
import sys

import requests
import xlrd

# reload(sys)
sys.setdefaultencoding('utf-8')

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


def read():
    workbook = xlrd.open_workbook("D:/PyProject/scripts/huize_insure/data/insures.xls")
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows

    caseCodes = [
                "0000004131001444",
                "0000004131101445",
                "0000004131301447",
                "0000004131201446",
                "0000052209502601",
                "0000052209502602",
                "0000052209502603"
                ]

    for index in range(1, nrows):
        prodName = str(sheet.cell(index, 1).value).strip()
        planName = str(sheet.cell(index, 2).value).strip()
        caseCode = str(sheet.cell(index, 3).value).strip()

        if caseCode not in caseCodes:
            continue

        if len(planName) > 0:
            prodName = prodName + '-' + planName

        jsonFile = 'data/' + caseCode + '.json';
        if os.path.exists(jsonFile):
            with open(jsonFile) as dataDetail:
                detail = json.load(dataDetail)
                dataFile = 'data/' + prodName.encode("gb2312") + '/'
                if not os.path.exists(dataFile):
                    os.mkdir(dataFile)

                    try:
                        # 主条款
                        mainProductTerms = detail['mainProductTerms']
                        mainTermFile = dataFile + '主条款'.encode("gb2312") + '/'
                        if not os.path.exists(mainTermFile):
                            os.mkdir(mainTermFile)

                        for term in mainProductTerms:
                            url = term['attachmentUrl']
                            title = term['title']
                            termFile = mainTermFile + title.encode("gb2312") + '.pdf'
                            data = requests.get(url, headers=headers, stream=True, timeout=30)
                            f = open(termFile, 'wb+')
                            f.write(data.content)
                            f.close()

                        # 附加条款
                        additionalProductTerms = detail['additionalProductTerms']
                        additionalFile = dataFile + '附加条款'.encode("gb2312") + '/'
                        if not os.path.exists(additionalFile):
                            os.mkdir(additionalFile)
                        for term in additionalProductTerms:
                            url = term['attachmentUrl']
                            title = term['title']
                            termFile = additionalFile + title.encode("gb2312") + '.pdf'
                            data = requests.get(url, headers=headers, stream=True, timeout=30)
                            f = open(termFile, 'wb+')
                            f.write(data.content)
                            f.close()

                        # 费率表
                        pictureRateTable = detail['pictureRateTable']
                        if len(pictureRateTable) > 0:
                            url = pictureRateTable;
                            title = (prodName + '-费率表.pdf').encode("gb2312")
                            rateFile = dataFile + title
                            data = requests.get(url, headers=headers, stream=True, timeout=30)
                            f = open(rateFile, 'wb+')
                            f.write(data.content)
                            f.close()

                        # 产品特色
                        features = detail['features']
                        if len(features) > 0:
                            pc = ''
                            h5 = ''
                            app = ''
                            title = (prodName + '-产品特色.txt').encode("gb2312")
                            featureFile = dataFile + title
                            for feature in features:
                                dataType = feature['dataType']
                                content = feature['content']
                                if int(dataType) == 1:
                                    pc += (content + ';')
                                elif int(dataType) == 2:
                                    h5 += (content + ';')
                                elif int(dataType) == 3:
                                    app += (content + ';')

                            f = open(featureFile, 'wb+')
                            f.write('PC: ' + pc + '\nH5: ' + h5 + '\nAPP: ' + app)
                            f.close()
                            pass

                        # 理赔案例
                        insuranceCase = detail['insuranceCase']
                        if len(insuranceCase) > 0:
                            title = (prodName + '-理赔案例.html').encode("gb2312")
                            insuranceCaseFile = dataFile + title
                            f = open(insuranceCaseFile, 'wb+')
                            f.write(str(insuranceCase).strip())
                            f.close()
                            pass
                    except:
                        print(caseCode)
                        pass
        else:
            print (u"缺少%s" % caseCode)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    read()
    pass
