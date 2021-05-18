import pyecharts.options as opts
from pyecharts.charts import *
import pandas as pd
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import csv

from pyecharts.globals import ThemeType
from pyecharts.render import display


colorlist = []
# 读取文件
with open ('../file_csv/娱乐区.csv','r',encoding='utf-8',)as file:
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
# 以弹幕颜色进行分组
for i in df.groupby('弹幕颜色'):
    print(i)
# 按使用各个弹幕颜色的数量进行排序
num = df.groupby(['弹幕颜色']).size()
nums = num.sort_values(ascending=False)
print(nums)
# 将得到的数量循环并整合成一个列表
lists= []
for i in nums:
    lists.append(i)
a = lists
print(a)
# 每个数量所对应的颜色信息
color_name = ['白色','红色','蓝色','粉色','紫罗兰红色','紫色','青色','酸橙绿','浅黄色','深粉色','银白色','沙棕色']

# 绘制饼图
c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK,))
    .add('',[list(z) for z in zip(color_name,a)],center=["50%", "55%"])
    .set_colors(["#EFEBDC", "red", "blue", "pink", "#933D50 ", "purple", "#327662",'#28713E','yellow','#D14152','white','brown'])
    .set_global_opts(
        title_opts=opts.TitleOpts(title='娱乐区弹幕颜色饼图',title_textstyle_opts=opts.TextStyleOpts(color="white"),pos_right=20),
        # 图例配置
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
        toolbox_opts=opts.ToolboxOpts(is_show=True,pos_bottom= 20),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True,formatter='{b}:{c}条')
    )
)
c.render('bing.html')