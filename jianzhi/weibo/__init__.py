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

"""
微博情感分析
https://blog.csdn.net/hzp666/article/details/78969150
https://blog.csdn.net/weixin_43717839/article/details/98073726
https://www.bilibili.com/video/av412884801/
https://github.com/ReainL/sina_comment
https://m.weibo.cn/single/rcList?format=cards&id=4627963633205346&type=comment&hot=0&page=2
https://m.weibo.cn/comments/hotflow?id=4627963633205346&mid=4627963633205346&max_id_type=0
"""
import re

# 正则表达式匹配IP
ip_str = """
<link rel="dns-prefetch" href="//34.193.236.201:80">
<link rel="dns-prefetch" href="//39.107.183.55:3128">
<link rel="dns-prefetch" href="//165.22.252.119:80">
<link rel="dns-prefetch" href="//3.221.105.1:80">
<link rel="dns-prefetch" href="//3.211.17.212:80">
<link rel="dns-prefetch" href="//202.108.22.5:80">
<link rel="dns-prefetch" href="//88.198.24.108:8080">
<link rel="dns-prefetch" href="//220.181.111.37:80">
<link rel="dns-prefetch" href="//189.206.105.163:80">
<link rel="dns-prefetch" href="//41.59.90.92:80">
<link rel="dns-prefetch" href="//3.211.65.185:80">
<link rel="dns-prefetch" href="//3.219.153.200:80">
<link rel="dns-prefetch" href="//191.96.42.80:8080">
"""

ips = re.findall(r"(\d+\.\d+\.\d+\.\d+)", ip_str)
print(ips)