# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/4/2 21:35
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:采集微博账号的推文数据
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import json
import random
import requests
import time
import MySQLdb

"""
Mysql的建表SQL语句如下：
CREATE TABLE `weibo_post` (
  `time` varchar(50) DEFAULT NULL,
  `post_id` varchar(50) DEFAULT NULL,
  `post_bid` varchar(50) DEFAULT NULL,
  `text` varchar(255) DEFAULT NULL,
  `likes` varchar(30) DEFAULT NULL,
  `comments` varchar(30) DEFAULT NULL,
  `reposts` varchar(30) DEFAULT NULL,
  `if_repost` varchar(30) DEFAULT NULL
) 

表新建好以后，程序运行
"""

UA = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0;\
       Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1))',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; 360SE)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
      'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 \
      (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) \
      Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) \
      Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; \
      .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; \
      .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',

      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) \
      Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0',

      'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) \
      Version/5.0.2 Mobile/8C148 Safari/6533.18.5',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)']


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
    sql = "insert into weibo_post values (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn = connect_db()
    with conn.cursor() as cursor:
        for i in data:
            return_data.append([i["time"], i["post_id"], i["post_bid"], i["text"], i["likes"], i["comments"], i["reposts"], i["if_repost"]])
        cursor.executemany(sql, return_data)
        conn.commit()
    cursor.close()


class Weibo:
    def __init__(self):
        # 微博默认domain值
        self.domain = "107603"
        # 微博用户ID
        self.user_id = "1654134123"
        self.post_list = []

    def get_html_data(self, page):
        # 实际请求Url
        actual_url = ("https://m.weibo.cn/api/container/getIndex?" +
                      "type=uid" +
                      "&value=" + self.user_id +
                      "&containerid=" + self.domain + self.user_id +
                      "&page=" + str(page))

        # 随机获取headers
        res = requests.get(actual_url, headers={'User-Agent': UA[random.randint(0, len(UA) - 1)]}).text
        print("抓取开始,第" + str(page) + "次下拉,实际请求Url:" + actual_url)
        return res

    def run(self):
        for page in range(1, 10):
            res = self.get_html_data(page)
            if not res:
                print("抓取完成...")
                return self.post_list
            try:
                res_json = json.loads(res)["data"]["cards"]
            except Exception:
                print("抓取数据格式异常！！！")
                return self.post_list
            for content in res_json[1:]:
                item = {}
                # 解析微博数据
                try:
                    # 微博账号内容信息全在这个标签之后
                    content = content["mblog"]
                    # 推文发布时间
                    item["time"] = content["created_at"]
                    # 推文ID
                    item["post_id"] = content["id"]
                    # 推文的BID
                    item["post_bid"] = content["bid"]
                    # 推文内容
                    item["text"] = content["text"].replace("\n", ";")
                    # 推文点赞数
                    item["likes"] = content["attitudes_count"]
                    # 推文评论数
                    item["comments"] = content["comments_count"]
                    # 推文转发数
                    item["reposts"] = content["reposts_count"]
                    # 推文是否为转发
                    item["if_repost"] = ("retweeted_status" in content)
                    self.post_list.append(item)
                except KeyError:
                    print("剖析json格式异常")
                    return self.post_list
            time.sleep(2)
        print(self.post_list)
        insert_in_db(self.post_list)


if __name__ == '__main__':
    weibo = Weibo()
    weibo.run()