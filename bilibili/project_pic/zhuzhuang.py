# coding:utf-8
import pyecharts.options as opts
from pyecharts.charts import *
import pandas as pd
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import csv

from pyecharts.globals import ThemeType
from pyecharts.render import display

'''某个视频弹幕发送前十名的用户做了柱状图'''

'''数码区'''
shumaqu_file =open('../file_csv/数码区.csv','r',encoding='utf-8')
csvReader = csv.reader(shumaqu_file)
shumaqu_size = []
for item in csvReader:
    shumaqu_size.append(item)
pf = pd.DataFrame(shumaqu_size,columns=['弹幕出现时间','弹幕格式','弹幕字体','弹幕颜色','弹幕时间','弹幕池','用户ID','rowID','弹幕信息'])
new_pf =pf.drop(labels=0,axis=0)

# print(new_pf)
user_data = new_pf.groupby('用户ID').size().sort_values(ascending=False)[0:19]
print(user_data)
list_data = user_data.tolist()
print(list_data)

user = user_data.index
print(user)

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
bar.add_xaxis(list(user))
bar.add_yaxis('弹幕量',list(user_data))
bar.set_global_opts(
    # 设置副标题
    title_opts=opts.TitleOpts(title='数码区某视频弹幕排行榜'),
    visualmap_opts=opts.VisualMapOpts(is_show=True,type_='color',min_=4,max_=18),
    xaxis_opts=opts.AxisOpts(
        # 设置x轴坐标轴刻度的长度和是否显示   #名字过长
        axistick_opts=opts.AxisTickOpts(is_show=True,),
        #名字过长
        axislabel_opts=opts.LabelOpts(rotate=-30),
        name='用户ID'


    ),
        # 设置y轴最大,最小值
        yaxis_opts=opts.AxisOpts(min_=4,max_=18,name='单位/条'),
         # 工具箱
         toolbox_opts=opts.ToolboxOpts(is_show=True)
)
bar.set_series_opts(
    label_opts=opts.LabelOpts(font_size=20,font_style='italic')

)
bar.render('zzt.html')







