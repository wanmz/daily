from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
import csv
import os
import re
import pandas as pd


def sandiantu():
    # x轴数据表示24小时
    hours = []
    for i in range(0, 24):
        hours.append('%02d' % i)

    # y轴表示时间段对应的弹幕数量
    values = [0 for _ in range(0, 24)]
    for item in deal_time:
        if item in hours:
            values[hours.index(item)] += 1

    c = (
        EffectScatter()
            .add_xaxis(hours)
            .add_yaxis("每小时弹幕数量", values, symbol=SymbolType.ARROW)
            .set_global_opts(title_opts=opts.TitleOpts(title="番剧每小时弹幕数量"),
                             xaxis_opts=opts.AxisOpts(name='小时'),
                             yaxis_opts=opts.AxisOpts(name='单位/条'),
                             visualmap_opts=opts.VisualMapOpts(is_show=True, type_='color', min_=0, max_=250),
                             )
            .set_series_opts(markpoint_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='min', name='最小值'),
                                                                    opts.MarkLineItem(type_='max', name='最大值'),
                                                                    opts.MarkLineItem(type_='average', name='平均值'),
                                                                    ]),
                             label_opts=opts.LabelOpts(is_show=False)



                             )
            .render("sdt.html")

    )


if __name__ == '__main__':
    data = pd.read_csv('../file_csv/鬼灭之刃1.csv', encoding='utf-8')
    data = data.dropna()
    barrage_time = data['弹幕时间戳'].values
    # 存放所有弹幕发送时间（小时）
    deal_time = []
    for item in barrage_time:
        temp = re.split(':', item)[0]
        try:
            temp = temp.split()
            deal_time.append(temp[3])
        except:
            continue
    sandiantu()
