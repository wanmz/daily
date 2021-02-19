# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/19 20:39
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @Description:回文数
-------------------------------------------------
"""


def is_palindrome(x):
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(is_palindrome(121))
