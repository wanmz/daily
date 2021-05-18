# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/22 21:11
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:pandas处理
-------------------------------------------------
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filepath = r'F:\analysis-study-data\eg1.xls'
# filepath = r'F:\\analysis-study-data\\eg1.xls'
# filepath = r'F:/analysis-study-data/eg1.xls'

try:
    # 读取excel文件
    df = pd.read_excel(filepath)
except FileNotFoundError:
    print("文件{0}不存在".format(filepath))
    exit(0)

# 打印读取的表格结果
# print(df)
# 读取前10行
# print(df.head(10))

# 列值
# print(df.columns)

# 获取单列的个数
# print(df["效期"].value_counts())

# 索引值
# print(df.index)

# 获取某单列值
pihao = [str(x) for x in df["批号"].values]
num = list(df["数量"].values)
name = list(df["品名"].values)

x = np.arange(len(pihao))
'''开始绘画柱形图'''
# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 柱图大小
width = 0.3

# 创建图形
fig, ax = plt.subplots()

# print(pihao)
# ax.bar(pihao, num, width, color='green')
# 取默认柱子大小
rects = ax.bar(name, num, color='green')

# Y轴标题
ax.set_ylabel('剩余量/个')


ax.set_title('产品剩余量情况')

# X轴坐标竖着放置
plt.xticks(rotation="vertical")


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


fig.tight_layout()

# 柱头加值更加清晰化
autolabel(rects)

# 展示
plt.show()
