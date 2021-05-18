# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/24 21:31
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:成交量分析
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\Administrator\Desktop\北京二手房.xls")

# 整合成交量数据
chengjiaoliang = df["成交量"].copy()
for i in range(len(chengjiaoliang)):
    item = chengjiaoliang.iloc[i].strip()
    try:
        chengjiaoliang.iloc[i] = int(re.findall(r"30天成交(\d+)套", item)[0])
    except:
        chengjiaoliang.iloc[i] = 0
df["成交量"] = chengjiaoliang
# print(chengjiaoliang)

# 把区和小区合并成"小区地址"

xq_addr = df["区"] + '-' + df["小区"]
# print(xq_addr)

df2 = pd.DataFrame(data={'小区地址': xq_addr, "成交量": chengjiaoliang})

# 只拿成交量大于0的小区
df2 = df2[df2["成交量"] > 8]
# print(df2.reset_index(drop=True))

# 算一下总共有多少个
# print(df2.value_counts().count())

# 按成交量排序
# df2.sort_values(by="成交量")

# 按成交量排序，ascending是否按升序排序，并索引重新排序，并删除旧索引
df2 = df2.sort_values(by="成交量", ascending=False).reset_index(drop=True)
# print(df2)

y_labes = df2["小区地址"]
x_labes = df2["成交量"]
# print(type(x_labes))

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 用ggplot的风格来画图
plt.style.use('ggplot')

# 设置画布2
fig3 = plt.figure(3, facecolor= 'black')

ax3 = fig3.add_subplot(1,1,1,facecolor='#4f4f4f',alpha=0.3)

# 配置图形
plt.barh(y_labes, x_labes)

#设置标题、x轴、y轴的标签文本
title = plt.title('30天内小区成交量超过8套分布图',fontsize = 18,color = 'yellow')
xlabel= plt.xlabel('套',fontsize = 12,color = 'yellow')
ylabel = plt.ylabel('小区',fontsize = 12,color = 'yellow')

# X轴刻度文本垂直摆放
# plt.xticks(rotation=180)

plt.show()
