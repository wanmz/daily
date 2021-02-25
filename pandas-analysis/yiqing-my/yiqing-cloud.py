# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 20:15
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:云图

-------------------------------------------------
"""
import requests
from pyecharts.charts import *
from pyecharts.globals import SymbolType
from pyecharts import options as opts


# 获取疫情数据
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

cloud = (
        # WordCloud(init_opts=opts.InitOpts(theme='dark'))
        WordCloud()
        .add('累计死亡人数', oversea_confirm, word_size_range=[20, 50], shape=SymbolType.DIAMOND)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False, color='#fff'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全球疫情累计死亡人数分布'),
        )
    )
cloud.render(path='全球疫情累计死亡人数分布.html')