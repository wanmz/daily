# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 23:59
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:全球图
-------------------------------------------------
"""
import requests
from pyecharts.charts import *
from pyecharts import options as opts


url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
# debug
# print(json.dumps(data, ensure_ascii=False))

oversea_confirm = []
for item in data['results']:
    if item['countryEnglishName']:
        oversea_confirm.append((item['countryEnglishName']
                                .replace('United States of America', 'United States')
                                .replace('United Kingdom', 'Greenland'),
                                item['deadCount']))

_max = max(item[1] for item in oversea_confirm)

world_map = (
        Map(init_opts=opts.InitOpts(theme='dark'))
        .add('累计死亡人数', oversea_confirm, 'world', is_map_symbol_show=False, is_roam=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False, color='#fff'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全球疫情累计死亡人数分布'),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=_max)
        )
    )
world_map.render(path='全球疫情累计死亡人数分布.html')