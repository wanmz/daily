# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 23:59
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:海南图-确认与治愈数
-------------------------------------------------
"""
import requests
from pyecharts.charts import *
from pyecharts import options as opts

hn_data = []
url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
for item in data['results']:
    if item['provinceShortName'] == '海南':
        hn_data = item['cities']
hb_bar = (
        Bar(init_opts=opts.InitOpts(theme='dark'))
        .add_xaxis([hd['cityName'] for hd in hn_data])
        .add_yaxis('累计确诊人数', [hd['confirmedCount'] for hd in hn_data])
        .add_yaxis('累计治愈人数', [hd['curedCount'] for hd in hn_data])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="海南新冠疫情确诊及治愈情况"),
            legend_opts=opts.LegendOpts(is_show=True)
                )
        )
hb_bar.render(path='海南新冠疫情图.html')