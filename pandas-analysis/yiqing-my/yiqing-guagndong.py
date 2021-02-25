# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/26 0:23
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:广东疫情图
-------------------------------------------------
"""
import requests
from pyecharts.charts import *
from pyecharts import options as opts

hn_data = []
url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
for item in data['results']:
    if item['provinceShortName'] == '广东':
        hn_data = item['cities']

data = [(i['cityName'] + '市', i['confirmedCount']) for i in hn_data]
# print(data)
_max = max(item[1] for item in data)

china_map = (
        Map(init_opts=opts.InitOpts(theme='dark'))
        .add('确诊人数', data, '广东', is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color='#ffffff'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="广东省疫情累计确诊人数地图"),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=_max,
                                              is_piecewise=True
                                              )
        )
)
china_map.render(path='广东省疫情累计确诊人数地图.html')