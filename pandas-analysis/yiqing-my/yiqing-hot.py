# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 23:59
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:热点图
-------------------------------------------------
"""
import requests, pyecharts
from pyecharts.charts import *
from pyecharts import options as opts

url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
cities_data = []
for item in data['results']:
    if item['countryName'] == '中国':
        if item['cities'] is not None:
            cities_data.extend(item['cities'])
hot_geo = (
        Geo(init_opts=opts.InitOpts(theme='dark'))
        .add_schema(maptype='china')
        .add('累计确诊人数',
             [(i['cityName'], i['currentConfirmedCount']) for i in cities_data
              if i['cityName'] in pyecharts.datasets.COORDINATES.keys()],
             type_='heatmap')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='中国疫情热力图',
                                     pos_left='left'),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              is_piecewise=False,
                                              range_color=['#0ff', '#0f0', '#ff0', '#f00'])
        )
)
hot_geo.render(path='中国疫情热力图.html')