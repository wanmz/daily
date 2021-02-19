# -*- coding:utf-8 -*-

# @Date         : 2021/2/19 8:50
# @Author       : wmzhong
# @Email        : 289241101@qq.com
# @description  : 竖线图

import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number = [6, 7, 6, 1, 2]

plt.bar(waters, buy_number)
plt.title('男性购买饮用水情况的调查结果')

plt.savefig("男性购买饮用水情况的调查结果.jpg")
plt.show()
