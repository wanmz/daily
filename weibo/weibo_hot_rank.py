# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/31 21:30
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:微博热搜
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import requests
import MySQLdb
from bs4 import BeautifulSoup
from datetime import datetime


"""
Mysql的建表SQL语句如下：
CREATE TABLE `weibo_hot` (
  `热搜排名` varchar(255) DEFAULT NULL,
  `热搜关键词` varchar(255) DEFAULT NULL,
  `热度` varchar(255) DEFAULT NULL,
  `热度标签` varchar(255) DEFAULT NULL,
  `日期` varchar(30) DEFAULT NULL
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
    sql = "insert into weibo_hot values (%s, %s, %s, %s, %s)"
    conn = connect_db()
    with conn.cursor() as cursor:
        for i in data:
            return_data.append([i["rank"], i["keyword"], i["heat"], i["icon"], i["time"]])
        cursor.executemany(sql, return_data)
        conn.commit()
    cursor.close()


class Weibo:
    def __init__(self):
        self.headers = {
        "Accept": "text/html,application/xhtml+xrequestsml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "s.weibo.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
        self.url = "https://s.weibo.com/top/summary"
        self.hot_list = []

    def get_html_data(self):
        res = requests.get(self.url, headers=self.headers).text
        return res

    def deal_html_data(self, res):
        res = BeautifulSoup(res, "lxml")
        # 遍历热搜的标签
        # #pl_top_realtimehot 根据id, > table > tbody > tr 逐层查找
        for item in res.select("#pl_top_realtimehot > table > tbody > tr"):
            # 按类名.td-01提取热搜排名
            _rank = item.select_one('.td-01').text
            if not _rank:
                continue

            # 按类名.td-02提取热搜关键词
            keyword = item.select_one(".td-02 > a").text

            # 提取热搜热度
            heat = item.select_one(".td-02 > span").text

            # 提取热搜标签
            icon = item.select_one(".td-03").text

            self.hot_list.append({"rank": _rank, "keyword": keyword, "heat": heat, "icon": icon, "time":
                                  datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        # print(self.hot_list)
        insert_in_db(self.hot_list)

    def run(self):
        res = self.get_html_data()
        self.deal_html_data(res)


if __name__ == '__main__':
    weibo = Weibo()
    weibo.run()
