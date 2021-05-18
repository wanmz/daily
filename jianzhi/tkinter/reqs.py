# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/18 0:28
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import time
from threading import Thread

atotal = 32  # 总文章数量
afini = 0  # 已读取的文章数量
cookiestr = ''  # cookie全局变量


def genInfoStr():  # 拼接信息字符串
    global atotal
    global afini
    infoStr = '正在获取('+str(afini)+'/'+str(atotal)+'):'
    per = int(atotal/15)
    fi = int(afini/per)
    for _ in range(fi):
        infoStr += '■'
    for _ in range(15-fi):
        infoStr += '□'
    return infoStr


def getAll(cookieStr):  # 获取全部
    t = Thread(target=getArticles, args=(cookiestr,))  # 多线程，避免锁死界面
    t.start()
    return 'getAll OK!'


def getImages():  # 获取图片列表
    return 'getImages OK!'


def getArticles(cookiestr):  # 获取文章内容
    global afini
    for _ in range(10):
        afini += 1
        time.sleep(1)
    return 'getArticles OK!'


def getArticlesList():  # 获取文章列表
    return 'getArticlesList OK!'


def getVolums():  # 获取文集列表
    return 'getVolums OK!'