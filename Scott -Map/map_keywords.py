# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/3 21:31
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import json
import requests
from urllib import parse


class Map(object):
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/weather/weatherInfo"
        self.key = "b4dc36fadc284db9b877006f7f3d9f60"
        self.city = ""

    def get_data(self):
        data = {"city": self.city, "key": self.key, "extensions": "base", "output": "json"}
        res = requests.get(self.url, data).json()
        return res

    # 官网 https://developer.amap.com/api/webservice/guide/api/weatherinfo
    def weather_report(self, res):
        if res["status"] != '1':
            print("Sorry {0} 天气获取ERROR!!!".format(self.city))
            return
        else:
            for _res in res["lives"]:
                print("{} {} 天气: {}, 气温: {}, {}风, 风力: {}, 湿度: {}。播报日期: {}".format(
                    _res["province"], _res["city"], _res["weather"], _res["temperature"],
                    _res["winddirection"], _res["windpower"], _res["humidity"], _res["reporttime"]
                ))

    def run(self, *args):
        self.city = args[0]
        res = self.get_data()
        self.weather_report(res)


if __name__ == '__main__':
    code = input("请输入地区编码: ")
    map = Map()
    map.run(code)
