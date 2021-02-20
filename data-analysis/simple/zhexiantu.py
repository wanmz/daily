# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/20 19:01
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description: matplotlib模块plot用法，实现绘画折线，点状等图
-------------------------------------------------
"""

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/20 11:22
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://www.cnblogs.com/wmzhong/
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:折线,点状图
-------------------------------------------------
"""

import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴坐标值
x_labels = ['2021-2-12', '2021-2-13', '2021-2-14', '2021-2-15', '2021-2-16', '2021-2-17', '2021-2-18', '2021-2-19']

# Y轴坐标值
y_data1 = [100, 800, 50, 200, 150, 300, 100, 10]
y_data2 = [600, 200, 250, 150, 700, 400, 300, 500]
y_data3 = [50, 300, 200, 100, 1000, 200, 300, 250]
y_data4 = {"x_labels": ['2021-2-12', '2021-2-13', '2021-2-14',
                        '2021-2-15', '2021-2-16', '2021-2-17', '2021-2-18', '2021-2-19'],
           "y_test": [600, 200, 250, 150, 700, 400, 300, 500]}
data5 = [['2021-2-12', '2021-2-13', '2021-2-14', '2021-2-15', '2021-2-16', '2021-2-17', '2021-2-18', '2021-2-19'],
         [600, 200, 250, 150, 700, 400, 300, 500],
         [50, 300, 200, 100, 1000, 200, 300, 250],
         [100, 800, 50, 200, 150, 300, 100, 10]]

# 设置Y轴标题
plt.ylabel("零花钱/元")

# 标题
plt.title("过年得压岁钱调查结果")

# 默认折线图
# plt.plot(x_labels, y_data1)

# 折角是蓝色圆点折线图
# plt.plot(x_labels, y_data1, 'bo')

# 以Y轴索引为X轴值实现折线图
# plt.plot(y_data1)

# 点状图
# plt.plot(y_data1, 'c.', linestyle='dashed')
# plt.plot(x_labels, y_data1, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)

# 获取y_data4字典x_labels为X轴，y_test为Y轴
# plt.plot("x_labels", "y_test", data=y_data4)

# 展示多条折线图1
# plt.plot(x_labels, y_data1)
# plt.plot(x_labels, y_data2)
# plt.plot(x_labels, y_data3)

# 展示多条折线图2, 若data5是二维数组，其中第一列为X轴，其余列为Y轴
# plt.plot(data5[0], data5[1], data5[2], data5[3])

# 展示多条折现图3,指定 [x], y, [fmt] 多个集合
# 设置X坐标尺寸大小，不设置会导致X轴显示过于拥挤，适度设置。
plt.tick_params(labelsize=8)
plt.plot(x_labels, y_data1, 'r--', x_labels, y_data2, '-g', x_labels, y_data3, '--')

# 设置图标
plt.legend(labels=["小明", "小红", "小华"])
plt.show()