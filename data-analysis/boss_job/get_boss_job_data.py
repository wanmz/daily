# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/23 22:19
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:获取boss直聘数据
-------------------------------------------------
"""
"""方法一"""
# import urllib.request
#
# url = "https://movie.douban.com/top250?format=text"
# req = urllib.request.Request(url)
# response = urllib.request.urlopen(req)
# result = response.read().decode('utf-8')
# print(result)

"""方法二"""
import requests
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}
# url = "https://movie.douban.com/top250?format=text" # 等价下面的
url = "https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20210217&st=env" # 等价下面的
response = requests.get(url, headers=headers).text
print(response)

"""方法三"""
# 参考链接: https://www.jb51.net/article/181041.htm
# import urllib.request
# import requests
# import time
# import ssl
# import random
#
# def openUrl(ip, agent):
#  headers = {'User-Agent': agent}
#  proxies = {'http' : ip}
#  data = requests.get("http://movie.douban.com/top250?format=text", headers=headers, proxies=proxies, verify=True)
#  print(data.text)
#  ssl._create_default_https_context = ssl._create_unverified_context
#  # print("Access to success.")
#
# #IP池
# #IP来源：
# # https://www.kuaidaili.com/free/
# def randomIP():
#  ip = random.choice(['120.78.78.141', '122.72.18.35', '120.92.119.229'])
#  return ip
#
# #User-Agent
# #User-Agent来源：http://www.useragentstring.com/pages/useragentstring.php
# def randomUserAgent():
#  UserAgent = random.choice(['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
#         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'])
#  return UserAgent
#
#
# if __name__ == '__main__':
#     # for i in range(10):
#     ip = randomIP()
#     agent = randomUserAgent()
#     openUrl(ip, agent)
#     time.sleep(1)
