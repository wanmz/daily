# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/4/8 21:56
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description: WeGame云顶之弈比赛记录爬虫：召唤师列表
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import os
import requests
import MySQLdb

"""
Mysql的建表SQL语句如下：
CREATE TABLE `summoner` (
  `tie` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `uuid` varchar(50) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `ranking` varchar(30) DEFAULT NULL,
  `points` varchar(30) DEFAULT NULL
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
    sql = "insert into summoner values (%s, %s, %s, %s, %s, %s, %s)"
    conn = connect_db()
    with conn.cursor() as cursor:
        for i in data:
            return_data.append([i["area_id"], i["tier"], i["name"], i["uuid"], i["area"], i["ranking"], i["points"]])
        cursor.executemany(sql, return_data)
        conn.commit()
    cursor.close()


class SummonerList:
    def __init__(self):
        self.url = "https://qt.qq.com/lua/mlol_battle_info/get_total_tier_rank_list?area_id={0}&offset={1}&sign={2}"

    def run(self, area_id, offset, sign):
        res = requests.post(self.url.format(str(area_id), str(offset), sign)).json()
        # print(res)

        # 对返回的数据做判断
        if "data" not in res or "player_list" not in res["data"]:
            return None

        # 解析返回的数据
        summoner_list = []
        for summoner_item in res["data"]["player_list"]:
            if "tier_title" not in summoner_item:
                continue
            if "name" not in summoner_item:
                continue
            if "uuid" not in summoner_item:
                continue
            if "ranking" not in summoner_item:
                continue
            if "league_points" not in summoner_item:
                continue
            summoner_list.append({
                "area_id": area_id,
                "tier": summoner_item["tier_title"],
                "name": summoner_item["name"],
                "uuid": summoner_item["uuid"],
                "area": 1,
                "ranking": summoner_item["ranking"],
                "points": summoner_item["league_points"]
            })
        insert_in_db(summoner_list)
        return summoner_list


if __name__ == '__main__':
    os.environ["NO_PROXY"] = "qt.qq.com"
    sn = SummonerList()
    # 请求召唤师列表
    # sign 是网页为了反爬虫而设下的签名值，每次请求都不一样，
    # 要爬取所有的数据，就要对sign的生成进行解析，才能每次发送正确的请求得到数据
    # 参考 https://blog.csdn.net/weixin_44808384/article/details/108713847
    for params_item in [
        [1, 0, "a1a1eeafef7deb237f2f5e6172958615"],  # 艾欧尼亚:第1页
        [1, 20, "c4deacb883f65f4680cb55d4e8e6d5fc"],  # 艾欧尼亚:第2页
        [1, 40, "93be8e36d35b7a1265f1483217c9cc15"],  # 艾欧尼亚:第3页
        [1, 60, "41879281bc8425c941c737c4ff3bde4a"],  # 艾欧尼亚:第4页
        [1, 80, "eabfa2d2b60bcdf6a7fac54f68129dd6"],  # 艾欧尼亚:第5页
        [1, 100, "19160e26e17143f1bb5539d55905819b"],  # 艾欧尼亚:第6页
        [2, 0, "0d3349fa69a1d6055611880d03edffcc"],  # 比尔吉沃特:第1页
        [6, 0, "7f97a096f76a405507af4e7f16dd0d35"],  # 德玛西亚:第1页
        [14, 0, "c18788e78d9b059a556de576c78a334c"],  # 黑色玫瑰:第1页
        [14, 20, "46b6c711db7d80a34b9278704583006d"]  # 黑色玫瑰:第2页
    ]:
        # 区，页数，签名
        print(sn.run(params_item[0], params_item[1], params_item[2]))
