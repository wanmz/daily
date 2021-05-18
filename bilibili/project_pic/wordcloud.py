import pyecharts.options as opts
from pyecharts.charts import WordCloud
import pandas as pd
import csv
import matplotlib.colors as colors
from pyecharts.globals import ThemeType


class zhishiqu_danmu:
    def __init__(self):
        pass
    def ciyuntu(self):
        pf = pd.read_csv('../file_csv/知识区.csv',encoding='utf-8')
        pf = pf['弹幕信息']
        # 获取弹幕信息
        pf_values = pf.value_counts().values
        # 获得数量
        pf_index = pf.value_counts().index
        # print(pf_index)
        # print(pf_values)
        # 创建列表用于存放弹幕信息
        pf_data = []
        pf_lastdata = []
        for i in range(len(pf_index)):
            pf_firstdata = []
            pf_firstdata.append(pf_index[i])
            # 筛选出条数大于1 的 弹幕信息
            if int(pf_values[i]) > 1:
                pf_firstdata.append(int(pf_values[i]))
                pf_data.append(pf_firstdata)

        print(pf_data)
        for i in pf_data:
            pf_lastdata.append(tuple(i))

        print(pf_lastdata)
        # 制作词云图
        wordcloud = (
            WordCloud(init_opts=opts.InitOpts(theme=ThemeType.DARK))
                .add(
                "",
                pf_lastdata,
                # 词云图字体大小范围
                word_size_range=[20, 100],
                # 字体风格
                textstyle_opts=opts.TextStyleOpts(font_family="Arial", ),
                # 阴影
                emphasis_shadow_color="white",
            )
            .set_colors(["#006400", "#4B0082", "#FF4500", "#D48265", "#D6A2E8", "#4cd137", "red", "#0097e6", "#purple"])
            .set_global_opts(title_opts=opts.TitleOpts(title="知识区视频弹幕词云图", title_textstyle_opts=opts.TextStyleOpts(color="white")),
                             toolbox_opts=opts.ToolboxOpts(is_show=True),)
        )
        return wordcloud

if __name__ == '__main__':
    zhishiqu_danmu().ciyuntu().render("word.html")

