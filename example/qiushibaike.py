# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/9 21:11
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:糗事百科爬虫
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""

import re
import json
from tqdm import tqdm
import time
import requests
import MySQLdb
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

"""
Mysql的建表SQL语句如下：
CREATE TABLE `qiushibaike` (
  `时间` varchar(255) DEFAULT NULL,
  `作者` varchar(255) DEFAULT NULL,
  `性别` varchar(255) DEFAULT NULL,
  `年龄` varchar(255) DEFAULT NULL,
  `今日糗事` varchar(255) DEFAULT NULL,
  `糗事点赞数` varchar(255) DEFAULT NULL,
  `糗事评论数` varchar(255) DEFAULT NULL,
  `详情链接` varchar(255) NOT NULL
) 

表新建好以后，程序运行
"""


def connect_db():
    try:
        coon = MySQLdb.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            db="wmzhong",
            port=3306,
            charset="utf8"
        )
        return coon
    except Exception as e:
        print ("Error: %s") % e
        return None


def insert_in_db(data):
    return_data = []
    sql = "insert into qiushibaike values (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn = connect_db()
    with conn.cursor() as cursor:
        for i in data:
            return_data.append([i["today"], i["actor"], i["sex"], i["age"],
                                i["content"], i["click"], i["review"], i["href"]])
            cursor.executemany(sql, return_data)
        conn.commit()
    cursor.close()


class Qiushi(object):
    def __init__(self):
        self.base_url = "https://qiushibaike.com/"
        self.detail = "8hr/page/"
        self.page = 1
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        }

    def get_html(self):
        page_url = self.base_url+self.detail + str(self.page)
        res = requests.get(page_url, headers=self.headers).text
        # print(res)
        return res

    def get_child_html(self, href):
        _sex = str()
        _age = int()
        child_url = self.base_url + href
        res = requests.get(child_url, headers=self.headers).text
        i_soup = BeautifulSoup(res, "html.parser")
        div_list = i_soup.find('div', class_='side-user-top')
        user_sex = div_list.find('span', class_=re.compile((r'side-fans-num (\w+)')))
        # print(user_sex)
        if user_sex:
            # 性别
            _sex = re.search(r'user(\w)', str(user_sex)).group()[-1]
            # 年龄
            _age = re.search(r'(\d+)', str(user_sex)).group()
        return {"sex": _sex, "age": _age}

    def deal_html_data(self, res):
        data = []
        msg_dict = dict()
        msg_dict['today'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        soup = BeautifulSoup(res, "html.parser")
        # li标签class属性有多种参数值，如item typs_video，item typs_multi等，采用正则
        li_list = soup.find_all('li', class_=re.compile((r'item typs_(\w+)')))
        for li in li_list:
            # 获取超链接
            msg_dict["href"] = li.find('a', class_='recmd-content').get('href')
            # 获取篇子题目
            msg_dict["content"] = li.find('a', class_='recmd-content').get_text()
            # 点赞数
            msg_dict["click"] = li.find_all('span')[0].get_text()
            # 作者姓名
            msg_dict["actor"] = li.find('span', class_='recmd-name').get_text()
            # print(li.find_all('span'))
            # 评论数
            msg_dict["review"] = li.find_all('span')[3].get_text() if len(li.find_all('span')) == 6 else str()

            # 访问子链接去获取作者信息
            user_dict = self.get_child_html(msg_dict["href"])
            msg_dict.update(user_dict)
            data.append(msg_dict.copy())
        return data

    def run(self):
        # 首页总共有13页数据,设置进度条总长度
        pbar = tqdm(total=13)
        for page in range(1, 14):
            res = self.get_html()
            data = self.deal_html_data(res)
            insert_in_db(data)
            # 每次更新进度条的长度
            pbar.update(1)
        # 关闭占用的资源
        pbar.close()


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()