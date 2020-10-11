#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 19:42
# @Author  : ZhangL

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 参考自: 十分钟的 pandas 入门教程（中文翻译）
# https://ericfu.me/10-minutes-to-pandas/


# print(pd.__version__)

t1 = pd.Series([1, 3, 5, np.nan, 7, 9])
# print(t1)

dates = pd.date_range(datetime.now().strftime('%Y%m%d'), periods=6)

# print(np.random.randn(6, 4))
df = pd.DataFrame(np.random.randn(6, 4), dates, columns=list('ABCD'))

# print(df)
# print([3] * 4)

df2 = pd.DataFrame({'A': 1,
                    'B': pd.Timestamp('20130112'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': np.str('foo')
                    })
# print(df2)
# print(df2.dtypes)
# print(df2.F)
# print(df2.info)

# print(df2.head(2))
# print(df2.tail(3))
# print(df.index)


# print(df.to_numpy())
# print(df2.to_numpy())

# print(df.A)
# print(df['A'])

# print(df)
# print(df[0:3])
# print(dates[0])
# print(df.loc[dates[0]])
# print(df.loc['2020-07-30'])
# print(df.loc['2020-07-30 00:00:00'])
# print(df.loc[dates[0:3],['B','D']])
# print(df.loc['2020-08-26':'2020-08-28',['B','D']])
# print(df.loc[:,['B','D']])

# 当有一个维度是标量（而不是范围或序列）的时候，选择出的矩阵维度会减少
# print(df.loc['2020-08-26',['A','B']])

# 如果对所有的维度都写了标量，不就是选出一个元素吗？ 这种情况通常用 at ，速度更快，
# print(df.loc['2020-08-26','A'])
# print(df.at['2020-08-26','A'])

# *************** iloc 通过整数下标选择********************
# print(df.iloc[0:3])
# print(df.iloc[0:3,0:3])
# print(df.iloc[[0,2,3],[1,2]])

# ************* 布尔值下标 ****************

# print(df.A > 0)
# print(df[df.A > 0])
# 没有填充的值等于 NaN
# print(df[df > 0])
# isin() 函数：是否在集合中
# df3 = df.copy()
# df3['E'] = ['one', 'two', 'three', 'four', 'five', 'six']
# print(df3)
# print(df3[df3['E'].isin(['one','three'])])


# ******************************Setting**************************
# 为 DataFrame 增加新的列，按 index 对应
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200825', periods=6))
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range(datetime.now().strftime('%Y%m%d'), periods=6))
# print(s1)
# df['F'] = s1
# print(df)


# print(df3 > 0)
# df3[df3 < 0] = -df3
# df3 = -df3
# print(df)

#  ********************* 缺失值 pandas 用 np.nan 表示缺失值。通常它不会被计算。 **************************
# Reindexing 允许你改变某个轴的 index（以下代码制造一个示例用的 DataFrame）
# df4 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# df4.loc[dates[0]:dates[1], 'E'] = 1
# print(df4)
# 丢弃有 NaN 的行
# print(df4.dropna())
# # 填充缺失值
# print(df4.fillna(0))


####################################################################
#############################  统计 #################################
# df[df<0] = -df
# print(df)
# print(df.mean())
# print(df.mean(1))
# print(df.apply(np.cumsum))

# print(df.apply(lambda x: x.max()-x.min()))
s = pd.Series(np.random.random_integers(0, 7, size=10))
# s = pd.Series(np.random.randn(0, 7, size=10))
# print(s)

# ###################################################################
# ########################  Merge ##############################
# Concat 简单地按行拼接
# print(np.random.randn(10, 4))
# df5 = pd.DataFrame(np.random.randn(10, 4))
# print(df5)
#
# pieces = [df5[3:7],df5[:3],df5[7:]]
# print(pieces)
#
# df6 = pd.concat(pieces)
# print(df6)

# Join 和 SQL 的 join 是一个意思
# left = pd.DataFrame({'name': ['tom', 'jack'], 'age': [18, 20]})
# right = pd.DataFrame({'name': ['tome', 'jack'], 'age': [30, 24]})
# print(left)
# print(right)
# merge = pd.merge(left, right, on='key')
# print(merge)

# Append 向 DataFrame 增加新的数据行
# df7 = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
# print(df7)
# s = df7.iloc[3].copy()
# s['C'] = 0.0
# print(s)
# print('**************************************************')
# # df8 = df7.append(s, ignore_index=True)
# df8 = df7.append(s)
# print(df8)
# print(df8.iloc[3])

# Grouping 和 SQL 中的 GROUP BY 类似，包括以下这几步：
# 根据某些规则，把数据分组
# 对每组应用一个聚集函数，把结果放在一个数据结构中
# df9 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
#                          'foo', 'bar', 'foo', 'foo'],
#                    'B': ['one', 'one', 'two', 'three',
#                          'two', 'two', 'one', 'three'],
#                    'C': np.random.randn(8),
#                    'D': np.random.randn(8)})
# print(df9)
# print(df9.groupby('A').sum())
# print(df9.groupby(['A','B']).sum())


# ###################################################################

# *********************  Reshape  *******************************
# Stack 层叠
# tuples = list(zip(*[
#     ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
#     ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
# ]))

# print(tuples)
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# print(index)
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# print(df)


# ######################## 时间序列 #######################################
rng = pd.date_range('1/1/2020', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ps = ts.to_period()
ps.to_timestamp()
# print(rng)
# print(ts)

# #########################  类别  ###########################################
# df10 = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6], 'raw_grade': ['a', 'b', 'b', 'a', 'a', 'e']})
# df10['grade'] = df10['raw_grade'].astype('category')
# print(df10['grade'])
#
# df10['grade'].cat.categories = ['very good', 'good', 'very bad']
# df10['grade'] = df10['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])
# print(df10['grade'])
#
# print(df10)
#
# print(df10.groupby('grade').size())

# ####################  图表 ###############################

# 对于 DataFrame，可以直接 plot
# plt.close('all')
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
# plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()
