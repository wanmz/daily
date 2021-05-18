# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 23:59
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:折线图，采用虚拟数据。
-------------------------------------------------
"""

from pyecharts.charts import *
from pyecharts import options as opts

x_data = ['2-06', '2-13', '2-20', '2-27', '3-05', '3-12', '3-19', '3-26', '4-02', '4-09', '4-17']
# 现有确诊
y1_data = [20677, 46537, 49156, 36829, 22695, 13171, 6287, 2896, 987, 351, 122]
# 累计治愈
y2_data = [817, 4131, 11788, 26403, 41966, 51533, 58381, 61731, 63612, 64236, 63494]
line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('现有确诊', y1_data, color='#10aeb5')
        .add_yaxis('累计治愈', y2_data, color='#e83132')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='中国疫情随时间变化趋势')
       ))

line.render(path='中国疫情折线图.html')