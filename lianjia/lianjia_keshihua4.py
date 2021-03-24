# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/24 22:30
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:东城区房价区间分布
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Pie

df = pd.read_excel(r"C:\Users\Administrator\Desktop\北京二手房.xls")

# 找到东城区的小区价格
dongcheng = df[df["区"] == "东城"]
# 校验数据是否正确
# print(dongcheng.info)


# print(dongcheng["价格"].map(int))

# 数据清洗
price = dongcheng["价格"].copy()
for i in range(len(price)):
    item = price.iloc[i].strip()
    # 替换掉非数字的字符串并转为0
    if not item.isdigit():
        price.iloc[i] = 0
    else:
        price.iloc[i] = int(item)
# 结果演示
# print(price)

# 去掉暂无价格的小区数据
price = price[price.values > 0]

# print(price.values)
print(len(price.values))
cnt1, cnt2, cnt3, cnt4, cnt5, cnt6 = 0, 0, 0, 0, 0, 0
for i in price.values:
    if 100000 <= int(i) < 150000:
        cnt1 += 1
    elif 80000 <= int(i) < 100000:
        cnt2 += 1
    elif 60000 <= int(i) < 80000:
        cnt3 += 1
    elif 40000 <= int(i) < 60000:
        cnt4 += 1
    elif 20000 <= int(i) < 40000:
        cnt5 += 1
    else:
        cnt6 += 1

lables = ["10万-15万/米", "6万-8万/米", "4万-6万/米", "2万-4万/米", "其他"]
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
print(cnt5)
print(cnt6)


c = (
    Pie()
    .add("", [list(z) for z in zip(lables, [cnt1, cnt2, cnt3, cnt4, cnt5, cnt6])])
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange"])
    .set_global_opts(title_opts=opts.TitleOpts(title="北京东城区二手房价格"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

)
c.render("pie_set_color.html")