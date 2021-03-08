import pyecharts.options as opts
from pyecharts.charts import Funnel
import pandas as pd
from pyecharts.globals import ThemeType


def rate_barrage(min_index, max_index=100):
    num = 0
    total = 0
    for x in csv_data['弹幕信息']:
        if (len(x) >= min_index) & (len(x) <= max_index):
            num += 1
        total += 1
    a = num / total
    return round(round(a, 4) * 100, 2)


if __name__ == '__main__':
    x_data = ["弹幕长度1-3的占比", "弹幕长度4-10的占比", "弹幕长度11-20的占比", "弹幕长度21-40的占比", "弹幕长度40+的占比"]
    y_data = []
    csv_data = pd.read_csv('../file_csv/鬼灭之刃8.csv', encoding='utf-8')
    csv_data = csv_data.dropna()
    # 弹幕长度1-3的占比
    y_data.append(rate_barrage(1, 3))
    # 弹幕长度4-10的占比
    y_data.append(rate_barrage(4, 10))
    # 弹幕长度11-20的占比
    y_data.append(rate_barrage(11, 20))
    # 弹幕长度21-40的占比
    y_data.append(rate_barrage(21, 40))
    # 弹幕长度41+的占比
    y_data.append(rate_barrage(41))
    y_data.sort(reverse=True)

    data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

    (
        Funnel(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add(
            series_name="弹幕长度分析",
            data_pair=data,
            gap=2,
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="弹幕长度分析", subtitle="数据真实可靠",pos_bottom=20))
            .render("ldt.html")
    )
