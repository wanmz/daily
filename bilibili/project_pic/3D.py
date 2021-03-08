from pyecharts import options as opts
from pyecharts.charts import Bar3D
import csv


# 读取数据
from pyecharts.globals import ThemeType


def Data():
    contentList = []
    with open('dsm2.csv', 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file)
        for item in csvReader:
            contentList.append(item)
    return contentList


# 生成对应的图表
def make3Dbar(contentList):
    bar = Bar3D(init_opts=opts.InitOpts(width='1000px', height='600px'))
    types = ['白色', '红色', '蓝色', '天空蓝色', '葡萄紫色']
    style_2018 = [0, 0, 0, 0, 0]
    style_2019 = [0, 0, 0, 0, 0]
    style_2020 = [0, 0, 0, 0, 0]
    for item in contentList:
        # 弹幕颜色
        type = item[3]
        # 年份
        time = item[4].split('/')[0]
        # 弹幕格式
        style = int(item[1])
        if type == '16777215':
            if time == '2018':
                style_2018[0] = style_2018[0] + style
            elif time == '2019':
                style_2019[0] = style_2019[0] + style
            elif time == '2020':
                style_2020[0] = style_2020[0] + style
        elif type == '15138834':
            if time == '2018':
                style_2018[1] = style_2018[1] + style
            elif time == '2019':
                style_2019[1] = style_2019[1] + style
            elif time == '2020':
                style_2020[1] = style_2020[1] + style
        elif type == '16707842':
            if time == '2018':
                style_2018[2] = style_2018[2] + style
            elif time == '2019':
                style_2019[2] = style_2019[2] + style
            elif time == '2020':
                style_2020[2] = style_2020[2] + style
        elif type == '16646914':
            if time == '2018':
                style_2018[3] = style_2018[3] + style
            elif time == '2019':
                style_2019[3] = style_2019[3] + style
            elif time == '2020':
                style_2020[3] = style_2020[3] + style
        elif type == '10546688':
            if time == '2018':
                style_2018[4] = style_2018[4] + style
            elif time == '2019':
                style_2019[4] = style_2019[4] + style
            elif time == '2020':
                style_2020[4] = style_2020[4] + style

    result = []
    for i in range(len(types)):
        item = []
        item.append(types[i])
        item.append('2018')
        item.append(style_2018[i])
        result.append(item)
    for i in range(len(types)):
        item = []
        item.append(types[i])
        item.append('2019')
        item.append(style_2019[i])
        result.append(item)
    for i in range(len(types)):
        item = []
        item.append(types[i])
        item.append('2020')
        item.append(style_2020[i])
        result.append(item)
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title='弹幕格式统计3D图',
            title_textstyle_opts=opts.TextStyleOpts(
                color="white"
            )
        ),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        visualmap_opts=opts.VisualMapOpts(is_show=True, type_='color',pos_bottom=20,pos_left=40,min_=0,max_=360),
    )
    bar.add('弹幕格式统计', result)
    bar.render('3D.html')
    print(style_2018, style_2019, style_2020)

if __name__ == '__main__':
    contentList = Data()
    make3Dbar(contentList)
