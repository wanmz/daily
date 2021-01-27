# -*- coding:utf-8 -*-

# @Date         : 2020/11/19 20:48
# @Author       : wmzhong
# @Email        : 289241101@qq.com
# @description  :

import sys
import json
import time
from common.common import connect_db
reload(sys)
sys.setdefaultencoding('utf8')

Path = "F:\\股票\\2020-12-8-周二\\"


# def conver_num(item):
#     if len(str(item)) < 2:
#         return item
#     if str(item).find('-'):
#         item = str(item)[1:]
#         if len(str(item)) >= 9:
#             res = round(float(item)/1000/1000/100, 2)
#             return '-'+str(res)+"亿"
#         elif len(str(item)) >= 5:
#             res = round(float(item)/1000, 2)
#             return '-'+str(res)+"万"
#         elif len(str(item)) < 5:
#             res = round(float(item), 2)
#             return '-'+str(res)
#     else:
#         if len(str(item)) >= 9:
#             res = round(float(item)/1000/1000/100, 2)
#             return str(res)+"亿"
#         elif len(str(item)) >= 5:
#             res = round(float(item)/1000, 2)
#             return str(res)+"万"
#         elif len(str(item)) < 5:
#             res = round(float(item), 2)
#             return str(res)


def main():
    return_data = []
    # decode解码成utf-8的
    filename = Path+"2020-12-8-行业板块.txt".decode('utf-8')
    # filename = Path+"2020-11-18-资金流向-个股资金流.txt"
    # 先按换行符分割成list
    init_data = open(filename, "r").read().splitlines()
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
    sql = "insert into 行业板块 values (%s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s)"
    for _res in res["diff"]:
        # _res['f2'] = conver_num(_res['f2'])
        # _res['f3'] = conver_num(_res['f3'])
        # _res['f62'] = conver_num(_res['f62'])
        # _res['f184'] = conver_num(_res['f184'])
        # _res['f66'] = conver_num(_res['f66'])
        # _res['f69'] = conver_num(_res['f69'])
        # _res['f72'] = conver_num(_res['f72'])
        # _res['f75'] = conver_num(_res['f75'])
        # _res['f78'] = conver_num(_res['f78'])
        # _res['f81'] = conver_num(_res['f81'])
        # _res['f84'] = conver_num(_res['f84'])
        # _res['f87'] = conver_num(_res['f87'])
        return_data.append([_res['f12'], _res['f14'], _res['f2']
                            , _res['f4'], str(_res['f3']) + '%'
                           , _res['f20'], str(_res['f8']) + '%', _res['f104']
                            , _res['f105'], _res['f140'], _res['f128']
                            , str(_res['f136']) + '%', _res['f208'], _res['f207']
                            , str(_res['f222']) + '%', time.strftime('%Y-%m-%d-%A', time.localtime())])
    cursor.executemany(sql, return_data)
    cursor.close()
    conn.commit()


if __name__ == '__main__':
    main()
