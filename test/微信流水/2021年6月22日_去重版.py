#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/22
import os

import pandas


def read_weixin(path):
    print(path)
    # dataframe = pandas.read_excel(path, nrows=20)
    dataframe = pandas.read_excel(path)
    return dataframe


def read_yuanshi(paths):
    dataframes = []
    for path in paths:
        print(path)
        # dataframe = pandas.read_csv(path, engine='python', nrows=10)
        dataframe = pandas.read_csv(path, engine='python')

        dataframe = dataframe.loc[dataframe['商品名称'].str.contains("金城·惠医保")]
        dataframe = dataframe[dataframe.groupby('微信订单号')['微信订单号'].transform('count') == 1]
        dataframe['微信订单号'] = dataframe['微信订单号'].str.replace('`','')

        dataframes.append(dataframe)
    return pandas.concat(dataframes, ignore_index=True)


def merge(weixin_df, yuanshi_df):
    weixin_df_duplicated = weixin_df.drop_duplicates(['商户支付流水号'])
    yuanshi_df_duplicated = yuanshi_df.drop_duplicates(['微信订单号'])

    result = pandas.merge(weixin_df_duplicated, yuanshi_df_duplicated,
                          how='outer', left_on="商户支付流水号", right_on='微信订单号',
                          indicator=True)
    return result


def save(result, weixin_only, yuanshi_only):
    if os.path.exists(weixin_only):
        os.remove(weixin_only)
    if os.path.exists(yuanshi_only):
        os.remove(yuanshi_only)

    print(weixin_only)
    result.loc[result['_merge'] == 'left_only'].to_excel(weixin_only, index=False)

    print(yuanshi_only)
    result.loc[result['_merge'] == 'right_only'].to_excel(yuanshi_only, index=False)


if __name__ == '__main__':
    weixin = "数据2/0623.xlsx"
    yuanshi = ["数据2/微信流水-3月-原始表.csv", "数据2/微信流水-4月-原始表.csv", "数据2/微信流水-5月-原始表.csv"]
    weixin_only = '结果/去重版-微信.xlsx'
    yuanshi_only = '结果/去重版-原始表.xlsx'

    # save(merge(read_weixin(weixin), read_yuanshi(yuanshi)), weixin_only, yuanshi_only)

    weixin_df = read_weixin(weixin)
    print("微信表:")
    print(weixin_df['商户支付流水号'])

    yuanshi_df = read_yuanshi(yuanshi)
    print("原始表:")
    print(yuanshi_df['微信订单号'])

    result = merge(weixin_df, yuanshi_df)

    save(result, weixin_only, yuanshi_only)
