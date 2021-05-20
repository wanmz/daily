# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/18 23:05
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""

import re
import time
import sys
import random
import requests
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np

from collect_ip import ua_list
from snownlp import SnowNLP
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
            .add("4631348612695678", self.json_data)
            .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(title_opts=opts.TitleOpts(title="4631348612695678"))
        )
        p.render("4631348612695678特斯拉维权女主称为自保谎称怀孕.html")


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
    sql = "insert into sina_comment values (%s, %s, %s, %s, %s)"
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(sql, [data[0], data[1], data[2],data[3], data[4]])
        # for i in data:
        #     return_data.append([i[0], i[1], i[2], i[3], i[4]])
        # cursor.executemany(sql, return_data)
        conn.commit()
    cursor.close()


def execute_select(sql):
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()


def read_comment():
    print('读取数据库中数据...read_comment')
    sina_li = []
    comment_li = []
    user_li = []
    sql_select = "SELECT * FROM sina_comment_4631348612695678"
    params = '1000'
    result = execute_select(sql_select)
    print(result)
    for res in result:
        print(res)
        if res not in sina_li:
            sina_li.append([res[0],
                            res[1],
                            res[2],
                            res[3],
                            res[4]])
            user_name = res[1]
            user_li.append(user_name)
            comment = res[3]
            if comment:
                comment_li.append(comment)
    return sina_li, comment_li, user_li

# def snownlp(comment):
#     print('自然语言处理NLP...snow_analysis')
#     sentimentslist = []
#     for li in comment:
#         s = SnowNLP(li)
#         print(li, s.sentiments)
#         sentimentslist.append(s.sentiments)
#     fig1 = plt.figure("sentiment")
#     plt.hist(sentimentslist, bins=np.arange(0, 1, 0.02))
#     plt.show()


def snownlp(comment):
    print('自然语言处理NLP...snow_analysis')
    zhongli_num = 0
    xiaoji_num = 0
    jiji_num = 0
    for li in comment:
        s = SnowNLP(li)
        print(li, s.sentiments)
        if s.sentiments > 0.54:
            jiji_num += 1
        elif 0.46 < s.sentiments:
            xiaoji_num += 1
        else:
            zhongli_num += 1
    total = xiaoji_num + jiji_num + zhongli_num

    print(jiji_num, zhongli_num, xiaoji_num)
    # data.append(["积极", jiji_num], ["中立", zhongli_num], ["消极", xiaoji_num])
    gp = Graph()
    # 数组合并
    gp.json_data = np.vstack((["积极", format(float(jiji_num)/float(total), '.2f')],
               ["中立", format(float(zhongli_num)/float(total), '.2f')],
               ["消极", format(float(xiaoji_num)/float(total), '.2f')]))
    # print(gp.json_data)
    gp.m_pie()


def sina(ips):
    print('新浪微博评论采集...sina')
    # 返回一个随机IP
    ip = random.choice(ips)
    # 指定微博推文
    uid = '4630019865840370'
    # url = 'https://m.weibo.cn/single/rcList?format=cards&id=' + uid + '&type=comment&hot=0&page={}'
    url = "https://m.weibo.cn/single/rcList"
    i = 100
    comment_num = 1  # 第几条评论
    # try:
    # for i in range(i+1, 67000):
    # for i in range(i+1, i+10): debug测试
    for i in range(2, 100):
        ip = random.choice(ips)
        proxies = {
            'http': ip
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "SINAGLOBAL=6359816227155.011.1610374552161; UOR=,,www.baidu.com; _ga=GA1.2.1144589740.1617371919; __gads=ID=b63f319ff42985a1:T=1617371916:S=ALNI_MYmbB8zsY_sZBOjdcVlvoT-1o8oDw; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhenF-3PeRZOCIFCrWjSDr35JpX5KMhUgL.Fo-NeozN1Ke4ShM2dJLoIEXLxK-LBo5L12qLxKqL1KnL12-LxKML1hnLBo2LxK-L1K5LB-eLxKqLB-BL12et; ALF=1652967308; SSOLoginState=1621431308; SCF=AgznAAaH_SDVZNKGJNRME3cQ2RfRkVfvkRZ4JbVSM-exKHCKwi84gwq98Mcv_HlcXzIIYARzo8Mxcze6EIrBYew.; SUB=_2A25NoWRcDeRhGeNJ6VAW-S3FzzuIHXVu19KUrDV8PUNbmtAKLU3GkW9NS_y3RhdUaRsCV_hT23_u7YlheaHKappC; wvr=6; _s_tentry=www.baidu.com; Apache=350269630059.76965.1621434869288; ULV=1621434869320:13:2:2:350269630059.76965.1621434869288:1621344155637",
            "Host": "m.weibo.cn",
            "Referer": "https://m.weibo.cn/status/" + uid,
            "User-Agent": random.choice(ua_list),
            "X-Requested-With": "XMLHttpRequest",
        }
        # print(proxies)
        try:
            data = {
                "format": "cards",
                "id": uid,
                "type": "comment",
                "hot": 0,
                "page": i
            }
            # print(url.format(i))
            # res = requests.get(url=url.format(i), headers=headers, proxies=proxies)
            # 构造get请求参数param为json格式，把html格式数据去掉
            res = requests.get(url=url, headers=headers, proxies=proxies, params=data)
            res.encoding = 'utf8'
            try:
                r = res.json()
                print(r)
            except:
                 continue
            content = r[0]['card_group']
            if res.status_code == 200:
                print('抓取第%s页评论' % i)
                for j in range(0, len(content)):
                    print('第%s条评论' % comment_num)
                    hot_data = content[j]
                    comment_id = hot_data['user']['id']  # 用户id
                    user_name = hot_data['user']['screen_name']  # 用户名
                    created_at = hot_data['created_at']  # 评论时间
                    # 评论内容
                    comment = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]', '',
                                     hot_data['text'])
                    like_counts = hot_data['like_counts']  # 点赞数
                    sql_params = [comment_id, user_name, created_at, comment, like_counts]
                    print(sql_params)
                    insert_in_db(sql_params)
                    comment_num += 1
                time.sleep(random.randint(2, 5))
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
            if not ips:
                print('ip 已失效')
                sys.exit()
            # 删除不可用的代理IP
            if ip in ips:
                ips.remove(ip)
    # except Exception as e:
    #     print(e)


# def main():
#     conn = None
#     try:
#         conn = connect_db()
#         if conn:
#             ips = []
#             for i in range(6000):
#                 # 每隔1000次重新获取一次最新的代理IP，每次可获取最新的100个代理IP
#                 if i % 1000 == 0:
#                     ips.extend(get_ip())
#             sina(conn, ips)
#     finally:
#         if conn:
#             conn.close()

def main():
    """代理地址1
    ips = ["159.203.61.169", "05.252.161.48", "78.47.16.54", "51.91.157.66", "191.96.42.80",
           "113.100.209.146", "45.64.22.24", "120.199.210.18", "005.252.161.48", "5.252.161.48",
           "75.119.144.28", "3.221.105.1", "176.9.119.170"]
           """

    ips = ["159.203.61.169", "05.252.161.48", "78.47.16.54", "51.91.157.66", "191.96.42.80",
           "113.100.209.146", "45.64.22.24", "120.199.210.18", "005.252.161.48", "5.252.161.48",
           "75.119.144.28", "3.221.105.1", "176.9.119.170"]

    """代理地址3
    ips = ['34.193.236.201', '39.107.183.55', '165.22.252.119', '3.221.105.1', '3.211.17.212',
           '202.108.22.5', '88.198.24.108', '220.181.111.37', '189.206.105.163', '41.59.90.92',
           '3.211.65.185', '3.219.153.200', '191.96.42.80']
           """
    # sina(ips)
    # 情感分析
    sina_list, comment_list, user_list = read_comment()
    snownlp(comment_list)


if __name__ == '__main__':
    main()