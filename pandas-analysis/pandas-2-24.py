# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/24 21:27
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
-------------------------------------------------
"""
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}
url = "https://movie.douban.com/top250"
response = requests.get(url, headers=headers).text
# print(response)
# 解析html文件
soup = BeautifulSoup(response, 'html.parser')
# print(soup)
# 拿到的html文件，我们所想要的ol标签中
ol = soup.ol
# 查找所有的li标签数据
li_arr = ol.find_all('li')
# 拿一条数据测试
li_first = li_arr[0]
# 获取排名
# print(li_first.em.text)
paiming = li_first.em.text
# 获取片名和链接
a_arr = li_first.find_all('a')[1]
# 获取片名
# print(a_arr.find_all("span"))
# for value in a_arr.find_all("span"):
#     print(value.text.strip())

# 获取人名
# print(li_first.p.text.strip())


# soup = BeautifulSoup(response,"html.parser")
# print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
# for tag in soup.find_all('div', class_='info'):
#    # print tag
#     m_name = tag.find('span', class_='title').get_text()
#     m_rating_score = float(tag.find('span', class_='rating_num').get_text())
#     m_people = tag.find('div', class_="star")
#     m_span = m_people.findAll('span')
#     m_peoplecount = m_span[3].contents[0]
#     m_url = tag.find('a').get('href')
#     print(m_name+"        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)

# df = pd.DataFrame(data)
# print(df)
# 年份的电影报告
# print(pd.value_counts(df["create_time"], sort=True).sort_index())
# du = pd.value_counts(df["create_time"], sort=True).sort_index()
# du.plot(kind="bar")
# plt.show()
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
# plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
# plt.rcParams['font.size'] = 12  # 字体大小
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
#
# du = pd.value_counts(df["m_rating_score"], sort=True)
# du.plot(kind="bar")
# plt.show()