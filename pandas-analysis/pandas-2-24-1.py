# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/24 21:28
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:爬取豆瓣T250数据实战
参考: https://www.cnblogs.com/xisheng/p/9130156.html
-------------------------------------------------
"""
import re
import requests
import MySQLdb
import numpy as np
from bs4 import BeautifulSoup


# 获取豆瓣电影TOP250数据
def get_douban_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    response = requests.get(url, headers=headers).text
    return response


# 取主演，演员，剧情等信息数据。
def del_child_data(child_data):
    child_dict = dict()
    child_dict["create_time"] = child_data.split('/')[0].strip()
    child_dict["location"] = child_data.split('/')[1].strip()
    # 去掉"剧情"字符串
    child_dict["story"] = child_data.split('/')[2].strip().replace("剧情", "")
    return child_dict


# 正则表达式处理导演和演员数据。
def del_actor_data(actor_data):
    actor_dict = dict()
    # 正则表达式取演员数据
    re_compiled = re.compile(r'导演:(?P<actor>.+)\s+.*\n(?P<other>.+)')
    matched = re_compiled.match(actor_data)
    gd = matched.groupdict()
    # 人员信息
    actor_dict["actor"] = gd['actor'].strip()
    # 剧情信息
    other = gd['other'].strip()

    child_dict = del_child_data(other)
    # actor_dict和child_dict 组合
    actor_dict.update(child_dict)
    return actor_dict


def del_html_data(response):
    data = []
    main_dict = dict()
    # 拆html文件
    soup = BeautifulSoup(response, "html.parser")
    # calss_释义：因为class是Python中特殊的一种字符，所以beautifulsoup中后面加一个_来做为区分
    for tag in soup.find_all('div', class_='info'):
        # print tag
        # 电影名
        main_dict["movie"] = tag.find('span', class_='title').get_text()

        # 评分
        main_dict["score"] = float(tag.find('span', class_='rating_num').get_text())

        # 评价人数
        m_people = tag.find('div', class_="star")
        m_span = m_people.findAll('span')
        # 如: 2291749人评价 只取纯数字部分
        main_dict["people_num"] = re.search(r"(\d+)", m_span[3].contents[0]).group()

        # 详情链接
        main_dict["info_url"] = tag.find('a').get('href')

        # 正则表达式处理导演和演员数据。
        # 本来这里要压缩收尾空格，然后去掉换行符，后要取导演主演数据，所以这里不处理。
        # m_actor = tag.find('p').get_text().strip().replace('\n', "")
        m_actor = tag.find('p').get_text().strip()

        # print(m_actor)
        actor_dict = del_actor_data(m_actor)

        # 两个字典合并
        main_dict.update(actor_dict)

        # DEBUG日志输出
        print(main_dict)

        # dict.copy() 字典复制
        data.append(main_dict.copy())

    return data


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
    return_data = []
    conn = connect_db()
    cursor = conn.cursor()
    sql = "insert into TOP250 values (%s, %s, %s, %s, %s, %s, %s, %s)"
    for i in data:
        return_data.append([i["movie"], i["score"], i["people_num"], i["info_url"],
                            i["actor"], i["create_time"], i["location"], i["story"]])
    cursor.executemany(sql, return_data)
    cursor.close()
    conn.commit()


if __name__ == '__main__':
    # url = "https://movie.douban.com/top250"
    # 取步长为25的等差序列数
    page_list = np.arange(0, 251, 25)
    for page in page_list:
        # print(page)
        url = "https://movie.douban.com/top250?start={0}&filter=".format(page)
        resp = get_douban_data(url)
        # print(resp)

        data = del_html_data(resp)
        # print(data)
        # 插入数据库
        insert_in_db(data)
    print("数据处理完成")
