# coding:utf-8
import pyecharts.options as opts
from pyecharts.charts import *
import pandas as pd
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import csv

from pyecharts.globals import ThemeType
from pyecharts.render import display

'''玫瑰图:以弹幕长度排序'''
colorlist = []
# 读取文件
with open ('../file_csv/动画区.csv','r',encoding='utf-8',)as file:
    csvReader =csv.reader(file)
    # 遍历文件数据并将其添加到列表里面
    for item in csvReader:
        colorlist.append(item)
# 将列表转换成数据块
data = pd.DataFrame(colorlist,columns=['弹幕出现时间','弹幕格式','弹幕字体','弹幕颜色','弹幕时间','弹幕池','用户ID','rowID','弹幕信息'])
# 删除行
df=data.drop(labels=0,axis=0)
# new_data.columns.name=['弹幕出现时间','弹幕格式','弹幕字体','弹幕颜色','弹幕时间','弹幕池','用户ID','rowID','弹幕信息']
print(df)
# 以弹幕信息的长度进行分组
info = df['弹幕信息']
lenth = []
for i in info:
    lenth.append(len(i))
lenth.sort(reverse = True)
# print(lenth)
pf = pd.DataFrame(lenth)
# 该弹幕信息长度(取从0长度到20长度的)有几条信息(从而判断出用户比较偏向于发多长的弹幕)
count = pf.groupby([0]).size()[:21]
print(count)
tiaoshu = []
for i in count:
    tiaoshu.append(i)
a = tiaoshu
print(a)

b = list(range(0,21))
print(b)

c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK,))
    .add('',[list(z) for z in zip(b,a)],center=["50%", "55%"], radius=["30%", "75%"],
        rosetype="area",)
    .set_colors(["#EFEBDC", "red", "blue", "pink", "#933D50 ", "purple", "#327662",'#28713E','yellow','#D14152','white','brown'])
    .set_global_opts(
        title_opts=opts.TitleOpts(title='弹幕信息长度玫瑰图',title_textstyle_opts=opts.TextStyleOpts(color="white"),pos_right=20),
        # 图例配置
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
        toolbox_opts=opts.ToolboxOpts(is_show=True,pos_bottom= 20),

    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True,formatter='长度为{b}的弹幕:{c}条')
    )
)
c.render('rose.html')

