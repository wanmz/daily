# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/22 22:26
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:房屋总量分析
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\Administrator\Desktop\北京二手房.xls")
# print(df.info)
# print(df.head(10))
# 提取DataFrame中"区"列，根据"房屋总量"列进行分组，最后对分好组的数据进行处理求均值
# house = df["房屋总量"]
# for i in range(len(house)):
#     item = i.replace("套", "")

# df["房屋总量"] = df["房屋总量"].replace("套", "")
# print(df["房屋总量"])
# group = df["房屋总量"].groupby(df["区"])
# print(group.mean())
# for k, v in group:
#     print(k,v)
house = df["房屋总量"].copy()
for i in range(len(house)):
    item = house.iloc[i].strip()
    house.iloc[i] = int(item[:-1])
    # print(item[:-1])
df["房屋总量"] = house

# print(df[["区", "房屋总量"]])
# print(house)
# print(df["房屋总量"].groupby(df["区"]).sum())
house = df["房屋总量"].groupby(df["区"]).sum()

#设置视图画布1
fig1 = plt.figure(1, facecolor = 'black')

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#在视图1中设置子图1,背景色灰色，透明度0.3(figure.add_subplot 和plt.suplot都行)
ax1 = fig1.add_subplot(2,1,1,facecolor='#4f4f4f',alpha=0.3)

#设置轴的颜色为白色
plt.tick_params(colors='white')

#画直方图
house.plot(kind='bar', rot=0, color="#ef9d9a")

#设置标题
title = plt.title('北京各区二手房分布图', fontsize=18, color='yellow')

#设置X轴轴标题
xlabel = plt.xlabel('区域', fontsize=14, color='yellow')

#设置Y轴轴标题
ylabel = plt.ylabel('二手房数量', fontsize=14, color='yellow')

# X轴刻度文本垂直摆放
plt.xticks(rotation="vertical")

#设置子图2，是位于子图1下面的饼状图
ax2 = fig1.add_subplot(2,1,2)

# print(house.index)
# print(house.values.sum())
# 制作饼图之前数据处理
labels = list(house.index)
sizes = list(house.values)
# for i in sizes:
#     t = i/house.values.sum()*100
#     print(t)

explode = tuple([0.1]+[0]*16)
#shadow，饼是否有阴影
plt.pie(sizes,  explode=explode, labels=labels, autopct='%1.1f%%', radius=10, shadow=True, textprops={'color':'yellow'})
# 确保画的饼是圆的
ax2.axis('equal')

plt.show()
