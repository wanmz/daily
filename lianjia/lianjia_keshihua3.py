# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/24 22:08
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:出租量分析
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\Administrator\Desktop\北京二手房.xls")

# 整合出租量数据
chuzu = df["出租量"].copy()
for i in range(len(chuzu)):
    item = chuzu.iloc[i].strip()
    try:
        chuzu.iloc[i] = int(re.search(r"(\d+)", item).group(0))
    except:
        chuzu.iloc[i] = 0
df["出租量"] = chuzu
# print(chuzu)

# 把区和小区合并成"小区地址"

xq_addr = df["区"] + '-' + df["小区"]
# print(xq_addr)

df2 = pd.DataFrame(data={'小区地址': xq_addr, "出租量": chuzu})

# 只拿出租量大于70的小区
df2 = df2[df2["出租量"] > 70]
# print(df2.reset_index(drop=True))

# 算一下总共有多少个
# print(df2.value_counts().count())

# 按出租量排序
# df2.sort_values(by="出租量")

# 按成交量排序，ascending是否按升序排序，并索引重新排序，并删除旧索引
df2 = df2.sort_values(by="出租量", ascending=False).reset_index(drop=True)
# print(df2)

y_labes = df2["小区地址"]
x_labes = df2["出租量"]
# print(type(x_labes))

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 设置画布2
fig2 = plt.figure(2, facecolor='black')

ax2 = fig2.add_subplot(1,1,1,facecolor='#4f4f4f',alpha=0.3)
#设置轴的颜色为白色
plt.tick_params(colors='white')

# 配置图形
plt.bar(y_labes, x_labes,color="#ef9d9a")

#设置标题、x轴、y轴的标签文本
title = plt.title('出租量大于70间的小区分布图',fontsize = 18,color = 'yellow')
xlabel= plt.xlabel('小区',fontsize = 12,color = 'yellow')
ylabel = plt.ylabel('间',fontsize = 12,color = 'yellow')

# X轴刻度文本垂直摆放
plt.xticks(rotation=90)

plt.show()