# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/11 20:42
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
# https://nbviewer.jupyter.org/github/jasonding1354/pyDataScienceToolkits_Base/blob/master/Pandas/%281%29pandas_introduction.ipynb
https://nbviewer.jupyter.org/github/jasonding1354/pyDataScienceToolkits_Base/blob/master/Pandas/%282%29dataframe_slice_selection.ipynb
-------------------------------------------------
"""
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# print(np.array([1, 2, 3]))
# print(np.ones(3))
# print(np.zeros(3))
# print(np.random.random(3))

# data = np.array([[1,2], [3,4],[5,6],[7,8]])
# one = np.ones((1,1))
# print(data+one)

# data = [1, 2, 3]
# print(data[0])
# print(data[1])
# print(data[0:2])
# print(data[1:])

# print(np.ones((2,3)))
# data = np.array([[1,2],[5,3],[4,6]])
# print(data.max(axis=0))
# print(data.max(axis=1))
# print(data.T)

data = np.array([1,2,3,4,5,6])
print(data.reshape(2,3))