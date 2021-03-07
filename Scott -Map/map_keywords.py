# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/6 21:45
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:关键词搜索
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

    @staticmethod
    def print_msg(res):
        cnt = 1
        for _res in res:
            print("********************{0}.rows********************".format(cnt))
            print("pname: %s" % _res[0])
            print("cityname: %s" % _res[1])
            print("type: %s" % _res[2])
            print("adname: %s" % _res[3])
            print("name: %s" % _res[4])
            print("location: %s" % _res[5])
            cnt += 1

    # https://restapi.amap.com/v3/place/text
    def del_place(self, res):
        data = []
        # print(json.dumps(res, ensure_ascii=False))
        if res["status"] != '1':
            print("Sorry {0} 关键词搜寻获取ERROR!!!".format(self.keywords))
            return
        else:
            for _res in res["pois"]:
                data.append([_res["pname"], _res["cityname"], _res["type"], _res["adname"], _res["name"], _res["location"]])
            return data

    def run(self, *args):
        cname = args[0].split()
        self.keywords = cname[0]
        if len(cname) > 1:
            self.city = cname[1]
        res = self.get_data()
        data = self.del_place(res)
        self.print_msg(data)


if __name__ == '__main__':
    place = MapPlace()
    keywords = input("请输入搜寻关键词信息(关键词+城市)\n")
    place.run(keywords)