from pyecharts import options as opts
from pyecharts.charts import Bar3D, Line
import csv
import os
import pandas as pd


# 折线图：我们可以爬一个番剧啊，x轴为第几集，y轴为弹幕数量，分析哪一集是这个番剧最火的集数
#
# 1.词云图：可以做一个了，根据弹幕信息来做  2：散点图：x轴弹幕时间，y轴弹幕数量
# 3.漏斗图：六个分类排行第一的视频，根据每个视频的弹幕数量做一个漏斗图，看哪个分类比较火
# 4.柱状图 ：弹幕前十名用户  5.饼图：弹幕字体

# 循环读文件
from pyecharts.globals import ThemeType


def csv_one(path_list):
    for i in path_list:
        fr = open(i, 'r', encoding='gbk').read()
        with open('all_file.csv', 'a') as fd:
            fd.write(fr)
            print(fd)
    fd.closed


# 每集弹幕数的折线图
def zhexiantu():
    numbers = []
    values = []
    for index, item in enumerate(path_list):
        data = pd.read_csv(item, encoding='utf-8')
        # 去除空数据
        data = data.dropna()
        sum = len(data)
        for x in data['弹幕信息']:
            if len(x) > 3:
                sum -= 1
        values.append(f'第{index + 1}集')
        numbers.append(sum * 12)
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK,))
            .add_xaxis(values)
            .add_yaxis("弹幕数量", numbers)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_show=True,type_='color',min_=5500,max_=8900),
            axispointer_opts=opts.AxisPointerOpts(is_show=True),
            title_opts=opts.TitleOpts(title="每集弹幕数的折线图"),
            xaxis_opts=opts.AxisOpts(name='集数'),
            yaxis_opts=opts.AxisOpts(name='弹幕数量(单位/条)'),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
        )




            .render("zxt.html")
    )
if __name__ == '__main__':
    # 返回父目录
    path = os.path.abspath('..')
    # 存储鬼灭之刃的12个csv文件路径
    path_list = []
    for i in range(1, 13):
        path_list.append(f"{path}\\file_csv\\鬼灭之刃{i}.csv")
    # print(path_list)
    # csv_one(path_list)
    # for index, item in enumerate(path_list):
    #     print(index, item)
    zhexiantu()
