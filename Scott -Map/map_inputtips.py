# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/6 22:48
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:输入提示
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import json
import requests


class MapPlace(object):
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/assistant/inputtips"
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
            print("所属区域: %s" % _res[0])
            print("详细地址: %s" % _res[1])
            print("名字: %s" % _res[2])
            print("坐标: %s" % _res[3])
            cnt += 1

    # https://restapi.amap.com/v3/assistant/inputtips
    def del_place(self, res):
        data = []
        # print(json.dumps(res, ensure_ascii=False))
        if res["status"] != '1':
            print("Sorry {0} 关键词搜寻获取ERROR!!!".format(self.keywords))
            return
        else:
            for _res in res["tips"]:
                if _res["id"]:
                    data.append([_res["district"], _res["address"], _res["name"], _res["location"]])
            return data

    def run(self, *args):
        cname = args[0].split()
        self.keywords = cname[0]
        print(len(cname))
        if len(cname) > 1:
            self.city = cname[1]
        res = self.get_data()
        data = self.del_place(res)
        self.print_msg(data)


if __name__ == '__main__':
    place = MapPlace()
    keywords = input("请输入搜寻关键词信息(关键词+城市)\n")
    place.run(keywords)