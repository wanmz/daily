# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/6 23:01
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:步行路线设计
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


class Walk(object):
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/direction/walking"
        self.key = "b4dc36fadc284db9b877006f7f3d9f60"
        self.origin = ""
        self.destination = ""

    def get_data(self):
        data = {"origin": self.origin, "key": self.key, "output": "json", "destination": self.destination}
        res = requests.get(self.url, data).json()
        return res

    # https://restapi.amap.com/v3/direction/walking
    @staticmethod
    def del_walk(res):
        # print(json.dumps(res, ensure_ascii=False))
        if res["status"] != '1':
            print("ERROR")
            return
        else:
            paths = res["route"]["paths"]
            for path in paths:
                cnt = 1
                # 总步行预计时间/分
                duration = round(int(path["duration"])/60, 0)
                # 总步行距离
                distance = path["distance"]
                print("预计花费时间: {0}分, 预计步行距离: {1}米".format(duration, distance))
                for _res in path["steps"]:
                    print("********************{0}.rows********************".format(cnt))
                    print("路段步行指示: %s" % _res["instruction"])
                    print("此路段距离: %s米" % _res["distance"])
                    print("此路段预计步行时间: %s分" % round(int(_res["duration"])/60, 0))
                    cnt += 1

    def run(self, *args):
        cname = args
        self.origin = cname[0]
        if len(cname) > 1:
            self.destination = cname[1]
        res = self.get_data()
        self.del_walk(res)


if __name__ == '__main__':
    walk = Walk()
    place = MapPlace()
    begin = input("请输入出发点(城市+关键词)")
    data = place.run(begin)
    begin = data["location"]

    end = input("请输入终点(城市+关键词)")
    data = place.run(end)
    end = data["location"]

    # 开始步行设计
    walk.run(begin, end)