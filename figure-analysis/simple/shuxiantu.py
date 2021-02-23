# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/19 21:56
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @Description:matplotlib绘画柱线图
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

"""
x_labels = ['2021-2-12', '2021-2-13', '2021-2-14', '2021-2-15', '2021-2-16', '2021-2-17', '2021-2-18', '2021-2-19']
guangfu = [1, 7, 4, 2, 20, 5, 8, 10]
jungong = [2, 19, 5, 10, 8, 4, 30, 14]
zhengquan = [0.5, 16, 9, 10, 2, 18, 30, 11]

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴位置
x = np.arange(len(x_labels))
# 柱图大小
width = 0.2

# 创建图形
fig, ax = plt.subplots()

ax.bar(x + width, guangfu, width, label='光伏概念')
ax.bar(x + width*2, jungong, width, label='军工概念')
ax.bar(x + width*3, zhengquan, width, label='证券概念')

# Y轴标题
ax.set_ylabel('每日资金入量/亿')
ax.set_title('概念股资金动账')

# X轴坐标显示，x + width*2 标识X轴刻度所在位置
ax.set_xticks(x + width*2)
ax.set_xticklabels(x_labels)

# 显示右上角图例
ax.legend()

# 自动调整子图参数以提供指定的填充。多数情况下没看出来区别
fig.tight_layout()

plt.show()

"""

# 柱子上加柱长

x_labels = ['2021-2-12', '2021-2-13', '2021-2-14', '2021-2-15', '2021-2-16', '2021-2-17', '2021-2-18', '2021-2-19']
guangfu = [1, 7, 4, 2, 20, 5, 8, 10]
jungong = [2, 19, 5, 10, 8, 4, 30, 14]
zhengquan = [0.5, 16, 9, 10, 2, 18, 30, 11]

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴位置,X轴刻度的大小
x = np.arange(0, 16, 2)
# 柱图大小
width = 0.4

# 创建图形
fig, ax = plt.subplots()

rects1 = ax.bar(x + width, guangfu, width, label='光伏概念')
rects2 = ax.bar(x + width * 2, jungong, width, label='军工概念')
rects3 = ax.bar(x + width * 3, zhengquan, width, label='证券概念')

# Y轴标题
ax.set_ylabel('每日资金入量/亿')
ax.set_title('概念股资金动账')

# X轴坐标显示，x + width*2 标识X轴刻度所在位置
ax.set_xticks(x + width * 2)
ax.set_xticklabels(x_labels)

# 显示右上角图例
ax.legend()


# 在*rects*的每个栏的上方附加一个文本标签，显示它的高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# 自动调整子图参数以提供指定的填充。多数情况下没看出来区别
fig.tight_layout()

plt.show()