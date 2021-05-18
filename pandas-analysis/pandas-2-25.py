# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 20:15
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:获取疫情数据。全球疫情累计死亡人数分布
# 参考链接:https://gallery.pyecharts.org/#/README
          https://pyecharts.org/#/zh-cn/intro
-------------------------------------------------
"""
import requests
from pyecharts.charts import *
from pyecharts import options as opts


# 获取疫情数据
url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
# 打印结果查看下
# print(json.dumps(data, ensure_ascii=False))

oversea_confirm = []
for item in data['results']:
    if item['countryEnglishName']:
        # 需要适配js的国家英文，采用replace替换。
        oversea_confirm.append((item['countryEnglishName']
                                .replace('United States of America', 'United States')
                                .replace('United Kingdom', 'Greenland'),
                                item['deadCount']))

_max = max(item[1] for item in oversea_confirm)

world_map = (
        # 调地图接口, opts.InitOpts初始化配置项, theme 设置背景主题
        Map(init_opts=opts.InitOpts(theme='dark'))
        # is_map_symbol_show: 是否显示标记图形, is_roam: 是否开启鼠标缩放和平移漫游
        .add('累计死亡人数', oversea_confirm, 'world', is_map_symbol_show=False, is_roam=False)
        # set_series_opts 系列配置，opts.LabelOpts：标签配置项，is_show是否展示标签文字
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False, color='#fff'))
        # set_global_opts 全局配置
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全球疫情累计死亡人数分布'),
            # opts.LegendOpts 是否展示图例
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=_max)
        )
    )
world_map.render(path='全球疫情累计死亡人数分布.html')