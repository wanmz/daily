# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/21 21:11
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:饼状图
-------------------------------------------------
"""

import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 扇形图例标识
labels = ['0-10岁', '10-20岁', '20-30岁', '30-40岁', '40-100岁']

# 扇形大小
sizes = [40, 30, 20, 5, 5]
# 第二块扇形偏移
explode = [0, 0.1, 0, 0, 0]

# 创建图形
fig, ax = plt.subplots()

# 开始画饼图
ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True)

# 取消扇形偏移
# ax.pie(sizes, autopct='%1.1f%%', shadow=True)

# 扇形图例标识于扇形边
# ax.pie(sizes, labels=labels, xplode=explode, autopct='%1.1f%%', shadow=True)

# 确保画的饼是圆的
ax.axis('equal')

ax.set_title('各年龄段长蛀牙情况')

# 设置图例
ax.legend(labels=labels)

plt.show()

