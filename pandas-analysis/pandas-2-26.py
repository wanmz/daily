# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/26 23:10
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:王者荣耀皮肤下载，英雄皮肤个数云图，英雄定位饼图
-------------------------------------------------
"""
import os
import time
import requests
from bs4 import BeautifulSoup
from urllib import parse
from pyecharts import options as opts
from pyecharts.charts import WordCloud, Pie


class Graph(object):
    def __init__(self):
        self.json_data = []

    def m_cloud(self):
        cloud = (
            WordCloud(init_opts=opts.InitOpts(theme='essos'))
            .add("英雄皮肤个数", self.json_data)
            .set_global_opts(title_opts=opts.TitleOpts(title="英雄皮肤个数分布"))
        )
        cloud.render("王者荣耀英雄皮肤个数.html")

    def m_pie(self):
        p = (
            Pie(init_opts=opts.InitOpts(theme='essos'))
            .add("英雄定位个数", self.json_data)
            .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(title_opts=opts.TitleOpts(title="英雄定位个数分布"))
        )
        p.render("英雄定位个数分布.html")


class Skin(object):
    chart_dict = {
        1: "战士",
        2: "法师",
        3: "坦克",
        4: "刺客",
        5: "射手",
        6: "辅助"
    }

    def __init__(self):
        self.hero_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.base_url = 'https://pvp.qq.com/web201605/herodetail/'
        self.detail_url = ''
        self.img_folder = 'skin'
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
        self.skin_detail_url = '116/116-bigskin-1.jpg'

    def get_hero(self):
        request = requests.get(self.hero_url)
        hero_list = request.json()
        return hero_list

    def get_skin_html(self):
        url = parse.urljoin(self.base_url, self.detail_url)
        request = requests.get(url)
        request.encoding = 'gbk'
        html = request.text
        soup = BeautifulSoup(html, 'lxml')
        skip_list = soup.select('.pic-pf-list3')
        return skip_list

    def get_hero_skin(self, hero_name, hero_no):
        skip_list = self.get_skin_html()
        for skin_info in skip_list:
            img_names = skin_info.attrs['data-imgname']
            name_list = img_names.split('|')
            skin_no = 1
            for skin_name in name_list:
                self.skin_detail_url = '%s/%s-bigskin-%s.jpg' % (hero_no, hero_no, skin_no)
                skin_no += 1
                img_name = hero_name + '-' + skin_name.split('&')[0] + str(skin_no-1) + '.jpg'
                self.download_skin(img_name)

    def download_skin(self, img_name):
        img_url = parse.urljoin(self.skin_url, self.skin_detail_url)
        # 防止http请求太快，导致异常
        time.sleep(0.5)
        request = requests.get(img_url)
        if request.status_code == 200:
            print('download-%s' % img_name)
            img_path = os.path.join(self.img_folder, img_name)
            with open(img_path, 'wb') as img:
                img.write(request.content)
        else:
            print('img error!')

    def make_folder(self):
        if not os.path.exists(self.img_folder):
            os.mkdir(self.img_folder)

    def hero_skin(self, hero_list):
        num = 0
        for hero in hero_list:
            num += 1
            hero_no = str(hero['ename'])
            self.detail_url = hero_no + '.shtml'
            hero_name = hero['cname']
            self.get_hero_skin(str(num) + hero_name, hero_no)

    def hero_skin_cloud(self, hero_list):
        graph = Graph()
        hero_skin_json = []
        for hero in hero_list:
            hero_no = str(hero['ename'])
            self.detail_url = hero_no + '.shtml'
            hero_name = hero['cname']
            skip_list = self.get_skin_html()
            for skin_info in skip_list:
                img_names = skin_info.attrs['data-imgname']
                name_list = img_names.split('|')
                hero_skin_json.append([hero_name, len(name_list)])
        graph.json_data = hero_skin_json
        graph.m_cloud()

    def hero_position_pie(self, hero_list):
        graph = Graph()
        position_dict = dict()
        num = int()
        for hero in hero_list:
            if hero['hero_type'] in position_dict.keys():
                position_dict[hero['hero_type']] += 1
            else:
                position_dict[hero['hero_type']] = num + 1

            if "hero_type2" in hero.keys():
                if hero['hero_type2'] in position_dict.keys():
                    position_dict[hero['hero_type2']] += 1
                else:
                    position_dict[hero['hero_type2']] = num + 1

        graph.json_data = [[self.chart_dict[i], position_dict[i]] for i in position_dict]
        graph.m_pie()

    def run(self):
        self.make_folder()
        hero_list = self.get_hero()
        # 英雄皮肤下载
        # self.hero_skin(hero_list)
        # 英雄皮肤个数云图
        self.hero_skin_cloud(hero_list)
        # 英雄定位分布图
        self.hero_position_pie(hero_list)


if __name__ == '__main__':
    skin = Skin()
    skin.run()
