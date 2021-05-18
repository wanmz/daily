# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/7 14:54
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:公交车路线
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import json
import requests


class MapPlace(object):
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/place/text"
        self.key = "b4dc36fadc284db9b877006f7f3d9f60"
        self.keywords = ""
        self.city = ""

    def get_data(self):
        data = {"keywords": self.keywords, "key": self.key, "extensions": "base", "output": "json", "city": self.city}
        res = requests.get(self.url, data).json()
        return res

    # https://restapi.amap.com/v3/place/text
    def del_place(self, res):
        # print(json.dumps(res, ensure_ascii=False))
        if res["status"] != '1':
            print("Sorry {0} 关键词搜寻获取ERROR!!!".format(self.keywords))
            return
        else:
            # 仅取一个
            return res["pois"][0]

    def run(self, *args):
        cname = args[0].split()
        self.city = cname[0]
        if len(cname) > 1:
            self.keywords = cname[1]
        res = self.get_data()
        data = self.del_place(res)
        return data


class Transit(object):
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/direction/transit/integrated"
        self.key = "b4dc36fadc284db9b877006f7f3d9f60"
        self.origin = ""
        self.destination = ""
        # 起点城市
        self.city = ""
        # 终点城市
        self.cityd = ""
        # 公交快捷方式
        self.strategy = 2
        # 是否夜班车
        self.nightflag = 0

    def get_data(self):
        data = {"origin": self.origin, "key": self.key, "destination": self.destination,
                "city": self.city, "cityd": self.cityd, "strategy": self.strategy}
        res = requests.get(self.url, data).json()
        return res

    # https://restapi.amap.com/v3/direction/walking
    @staticmethod
    def del_walk(res):
        print(json.dumps(res, ensure_ascii=False))
        if res["status"] != '1':
            print("ERROR")
            return
        else:
            print("此段路程距离:{0}米，出租车费用:{1}".format(res["route"]["distance"], res["route"]["taxi_cost"]))
            # 待解析

    def run(self, *args):
        self.city = args[0]
        self.origin = args[1]
        self.cityd = args[2]
        self.destination = args[3]

        res = self.get_data()
        self.del_walk(res)


if __name__ == '__main__':
    transit = Transit()
    place = MapPlace()
    begin = input("请输入出发点(城市+关键词)")
    begin_data = place.run(begin)

    end = input("请输入终点(城市+关键词)")
    end_data = place.run(end)

    # 开始公交车设计
    transit.run(begin_data["cityname"], begin_data["location"], end_data["cityname"], end_data["location"])
