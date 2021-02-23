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


'''同时绘制四个饼图
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]

# 创建四个饼图型
fig, axs = plt.subplots(2, 2)

# 第一个饼图设置
axs[0, 0].pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

# 第二个饼图设置，设置第二个扇形偏移
axs[0, 1].pie(fracs, labels=labels, autopct='%.0f%%', shadow=True,
              explode=(0, 0.1, 0, 0))

# 第三个饼图设置，设置更小半径及图例大小
patches, texts, autotexts = axs[1, 0].pie(fracs, labels=labels,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=True, radius=0.5)
# 第三个饼图设置，设置百分比图例大小参数
plt.setp(autotexts, size='x-small')
# 第一个扇形百分比值颜色设置
autotexts[0].set_color('white')

# 第四个饼图设置，设置更小半径及图例大小，第二个扇形偏移
patches, texts, autotexts = axs[1, 1].pie(fracs, labels=labels,
                                          autopct='%.0f%%',
                                          textprops={'size': 'smaller'},
                                          shadow=False, radius=0.5,
                                          explode=(0, 0.05, 0, 0))
# 对饼图设置属性值，设置扇形值大小
plt.setp(autotexts, size='x-small')

# 对饼图设置属性值，第一个扇形值设置为白色
autotexts[0].set_color('white')

plt.show()
'''

