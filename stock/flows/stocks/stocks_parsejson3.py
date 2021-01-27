# -*- coding:utf-8 -*-

# @Date         : 2020/11/17 23:33
# @Author       : wmzhong
# @Email        : 289241101@qq.com
# @description  :

import sys
import json
from common.common import connect_db
# reload(sys)
# sys.setdefaultencoding('utf8')

Path = "F:\\股票\\2020-11-18-周三\\"


def main():
    return_data = []
    # decode解码成utf-8的
    # filename = Path+"2020-11-18-资金流向-个股资金流.txt".decode('utf-8')
    filename = Path+"2020-11-18-资金流向-个股资金流.txt"
    # 先按换行符分割成list
    init_data = open(filename, encoding='utf-8').read().splitlines()
    data = init_data[0].split('\"data\":')
    # data[1]是得到切割后的数据
    # print data[1].decode("utf-8")
    # 取从后三位开始至首位字符串
    # print data[1][:-3]
    jdata = data[1][:-3]
    res = json.loads(jdata)
    # 打印res出来是unicode编码,显示问题不用管
    # print res
    # ensure_ascii=False 转成字符串时防止出现乱码
    # new_result = json.dumps(res, ensure_ascii=False)
    # print new_result
    # print res["diff"]
    conn = connect_db()
    cursor = conn.cursor()
    sql = "insert into 个股资金流 values (%s,%s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
    for _res in res["diff"]:
        return_data.append([_res['f12'], _res['f14'], _res['f2'], _res['f3'], _res['f62']
                           , _res['f184'], _res['f66'], _res['f69'], _res['f72'], _res['f75']
                           , _res['f78'], _res['f81'], _res['f84'], _res['f87']])
    cursor.executemany(sql, return_data)
    cursor.close()
    conn.commit()
    # cursor.close()
    # conn.commit()
    # coon = connect_db()
    # cursor = coon.cursor()
    # # sql = "insert into userinfo values('小弟', '23','男')"
    # sql = "select * from userinfo ;"
    # cursor.execute(sql)
    # # cursor.close()
    # # coon.commit()
    # rows = list(cursor.fetchall())
    # print rows


if __name__ == '__main__':
    main()
