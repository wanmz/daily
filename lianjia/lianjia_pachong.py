# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/22 17:48
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re
import json
import requests
import random
import threading
import MySQLdb
from bs4 import BeautifulSoup
from tqdm import tqdm

"""
SQL如下：
create table xiaoqu(
    区  varchar(50),
    小区 varchar(100),
    户型 varchar(100),
    成交量 varchar(100),
    出租量	varchar(100),
    区域	varchar(255),
    次区域	varchar(100),
    中介	varchar(20),
    房屋总量	varchar(100),
    价格(元/m2)	varchar(255)
)
"""


#Some User Agents
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

regions=[u"东城",u"西城",u"朝阳",u"海淀",u"丰台",u"石景山","通州",u"昌平",u"大兴",u"亦庄开发区",u"顺义",u"房山",u"门头沟",u"平谷",u"怀柔",u"密云",u"延庆",u"燕郊"]


# 简单数据库链接
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
    conn = connect_db()
    cursor = conn.cursor()
    sql = "insert into xiaoqu values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, data)
    cursor.close()
    conn.commit()


def xiaoqu_spider(region, url_page=u"http://bj.lianjia.com/xiaoqu/pg1rs%E6%98%8C%E5%B9%B3/"):
    """
    爬取页面链接中的小区信息
    """
    try:
        req = requests.get(url_page, headers=hds[random.randint(0, len(hds) - 1)])
        source_code = req.text
        soup = BeautifulSoup(source_code, "html.parser")
    except Exception as e:
        print(e)
        return
    xiaoqu_list = soup.findAll('li', {'class': 'clear xiaoquListItem'})
    for xq in xiaoqu_list:
        xq_name = ''.join(re.findall(r"<a.+target.+>(\w+)</a>", str(xq)))
        huxing = ''.join(re.findall(r"<a.+huxing.+>(\w+)</a>", str(xq)))
        chengjiaoliang = ''.join(re.findall(r"<a.title=.+网签.>(\w+)</a>", str(xq)))
        zufang = ''.join(re.findall(r"<a.*title=.+租房.>(\w+)</a>", str(xq)))
        quyu = xq.find('a', {'class': 'district'}).get_text() if xq.find('a', {'class': 'district'}) else str()
        i_quyu = xq.find('a', {'class': 'bizcircle'}).get_text() if xq.find('a', {'class': 'bizcircle'}) else str()
        xiaoshou = xq.find('a', {'class': 'agentName'}).get_text() if xq.find('a', {'class': 'agentName'}) else str()
        totalcount = xq.find('a', {'class': 'totalSellCount'}).get_text() if xq.find('a', {'class': 'totalSellCount'}) else str()

        price = xq.find('div', {'class': 'totalPrice'}).find('span').get_text()
        # xq_data.append([xq_name, huxing, chengjiaoliang, zufang, quyu, i_quyu, xiaoshou, totalcount, price])
        insert_in_db([region, xq_name, huxing, chengjiaoliang, zufang, quyu, i_quyu, xiaoshou, totalcount, price])


def do_xiaoqu_spider(region=u"昌平"):
    """
    爬取大区域中的所有小区信息
    """
    url = u"http://bj.lianjia.com/xiaoqu/rs" + region + "/"
    try:
        req = requests.get(url, headers=hds[random.randint(0, len(hds) - 1)])
        source_code = req.text
        soup = BeautifulSoup(source_code, "html.parser")
    except Exception as e:
        print(e)
        return
    d = soup.find('div', {'class': 'page-box house-lst-page-box'}).get('page-data')
    # print(type(d))
    total_pages = json.loads(d)['totalPage']
    # print(total_pages)
    for i in range(total_pages):
        url_page = u"http://bj.lianjia.com/xiaoqu/pg%drs%s/" % (i + 1, region)
        t = threading.Thread(target=xiaoqu_spider, args=(region, url_page))
        t.start()
        # t.join()


if __name__ == '__main__':
    # 爬下所有的小区信息
    pbar = tqdm(total=len(regions))
    for region in regions:
        try:
            do_xiaoqu_spider(region)
            # 每次更新进度条的长度
            pbar.update(1)
        except Exception:
            continue
    # 关闭占用的资源
    pbar.close()