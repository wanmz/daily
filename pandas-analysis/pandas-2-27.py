# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/27 21:48
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
1.2021年春节档电影票房走势
2.2021年春节档票房占比
# @公众号    :Python与数据分析之美
# 参考数据：猫眼http://piaofang.maoyan.com
-------------------------------------------------
"""
import datetime
import requests
from pyecharts import options as opts
from pyecharts.charts import Line, Pie


class Graph(object):
    def __init__(self):
        self.json_data = []

    def m_pie(self):
        p = (
            Pie(init_opts=opts.InitOpts(theme='dark'))
            .add("当天电影票房占比", self.json_data)
            .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(title_opts=opts.TitleOpts(title="当天电影票房占比", pos_bottom="5"))
        )
        p.render("当天电影票房占比.html")


class BoxRate(object):
    def __init__(self):
        self.box_rate_url = "http://piaofang.maoyan.com/dashboard-ajax/movie?orderType=0&showDate="
        self.box_date = str()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        }
        self.movieid = int()
        # 以这几部电影为例参考。
        self.movie_dict = {
            1299372: "你好，李焕英",
            1217023: "唐人街探案3",
            1300936: "人潮汹涌",
            1048268: "刺杀小说家",
            1299124: "新神榜：哪吒重生",
            1298938: "熊出没·狂野大陆",
            1199007: "侍神令"
        }

    def get_box_data(self, days):
        des_date = self.get_date(days=days)
        url = self.box_rate_url + des_date
        box_dict = requests.get(url, headers=self.headers).json()
        return des_date, box_dict

    def del_box_rate(self, box_dict):
        movie = []
        if "list" in box_dict["movieList"].keys():
            box_list = box_dict["movieList"]["list"]
            for _box in box_list:
                if _box["movieInfo"]["movieId"] == self.movieid:
                    movie.append(_box["sumBoxDesc"][:-1])
            return movie

    @staticmethod
    def get_date(days=0):
        return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y%m%d")

    def date_box_list(self):
        date_list = []
        movie_list = []
        # 倒着取值, 左闭右开，步长
        for period in range(7, -1, -1):
            des_date, box_dict = self.get_box_data(days=period)
            movie = self.del_box_rate(box_dict)
            date_list.append(des_date)
            movie_list.extend(movie)
        return date_list, movie_list

    def box_thread(self):
        date_list = []
        s1299372 = list()
        s1217023 = list()
        for k, v in self.movie_dict.items():
            if k == 1299372:
                self.movieid = 1299372
                date_list, s1299372 = self.date_box_list()
            elif k == 1217023:
                self.movieid = 1217023
                date_list, s1217023 = self.date_box_list()

        line = (
                Line()
                .add_xaxis(date_list)
                .add_yaxis("你好，李焕英", s1299372, color="blue")
                .add_yaxis("唐人街探案3", s1217023, color="black")
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="票房走势图", title_textstyle_opts=opts.TextStyleOpts(font_size=14)),
                    yaxis_opts=opts.AxisOpts(
                        axislabel_opts=opts.LabelOpts(formatter="{value}/亿"),
                    )
                )
        )
        line.render("票房走势图.html")

    def del_show_count(self, box_dict):
        if "list" in box_dict["movieList"].keys():
            box_list = box_dict["movieList"]["list"]
            for _box in box_list:
                if _box["movieInfo"]["movieId"] == self.movieid:
                    return _box["boxRate"][:-1]

    def show_count(self):
        data = []
        graph = Graph()
        for k, v in self.movie_dict.items():
            self.movieid = k
            des_date, box_dict = self.get_box_data(days=0)
            movie = self.del_show_count(box_dict)
            data.append((v, movie))
        graph.json_data = data
        print(graph.json_data)
        graph.m_pie()

    def run(self):
        # 票房走势
        # self.box_thread()
        # 当天电影票房占比
        self.show_count()


if __name__ == "__main__":
    box = BoxRate()
    box.run()