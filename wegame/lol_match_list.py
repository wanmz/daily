# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/4/11 11:29
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:英雄联盟比赛包含场次列表
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""

import requests
from bs4 import BeautifulSoup


class LOL:
    def __init__(self):
        self.url = "https://www.wanplus.com/schedule/%s.html"
        self.hearders ={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.wanplus.com/lol/schedule",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }

    def run(self, *args):
        match_id_list = []
        response = requests.get(self.url % args[0], headers=self.hearders).text
        bs = BeautifulSoup(response, "lxml")
        _labels = bs.select("body > div > div.content > div.left > div:nth-of-type(1) > div > a")
        for game_label in _labels:
            if game_label.has_attr("data-matchid"):
                match_id_list.append(game_label["data-matchid"])
        return [{
            "race_id": args[0],
            "match_id_list": match_id_list
        }]


if __name__ == '__main__':
    # 场次ID
    i_id = "68482"
    lol = LOL()
    print(lol.run(i_id))
