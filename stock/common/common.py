# -*- coding:utf-8 -*-

# @Date         : 2020/11/17 23:14
# @Author       : wmzhong
# @Email        : 289241101@qq.com
# @description  :

import MySQLdb


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
