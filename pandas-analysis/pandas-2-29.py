# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/2 23:07
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re
import requests
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline


class Tiobe(object):
    def __init__(self):
        self.url = "https://www.tiobe.com/tiobe-index/"

    def deal_data_html(self):
        date_list = list()
        return_data = []
        names = []
        res = requests.get(self.url).text
        content = ''.join(re.findall(r'series: (.*?)\}\);', res, re.DOTALL))
        content = re.findall(r'({.*?})', content, re.DOTALL)
        for line in content:
            name = ''.join(re.findall(r"{name : '(.*?)'", line))
            names.append(name)
            data = re.findall(r"\[Date.UTC(.*?)\]", line)
            for i_data in data:
                i_data = re.sub(r'[()]', "", i_data)
                value = i_data.split(',')[-1].strip()
                date = '-'.join(map(lambda x: x.strip(), i_data.split(',')[:-1]))
                if name == "Java":
                    date_list.append(date)
                return_data.append({date: {name: value}})
        # print(return_data)

        # 赋值初始化
        msg_dict = {i: {j: 0 for j in names}for i in date_list}
        # print(msg_dict)
        # 给字典赋实际值
        for k, v in msg_dict.items():
            for i in return_data:
                for i_k, i_v in i.items():
                    if k == i_k:
                        v.update(i_v)
        # print(msg_dict)
        return msg_dict

    @staticmethod
    def line_bar(msg_dict):
        t1 = Timeline().add_schema(play_interval=200)
        for date, msg in msg_dict.items():
            bar = (
                Bar()
                .add_xaxis(['C', 'Java', 'Python', 'C++', 'C#', 'Visual Basic', 'JavaScript', 'PHP', 'SQL', 'Assembly language'])
                .add_yaxis("语言热门度", [msg[key] for key in msg.keys()], label_opts=opts.LabelOpts(position="right"))
                .reversal_axis()
                .set_global_opts(title_opts=opts.TitleOpts("20年编程语言排名 {}".format(date)),
                                 legend_opts=opts.LegendOpts(is_show=False)
                )
            )
            t1.add(bar, date)
        t1.render("20年编程语言排名.html")

    def run(self):
        msg_dict = self.deal_data_html()
        self.line_bar(msg_dict)


if __name__ == '__main__':
    tiobe = Tiobe()
    tiobe.run()