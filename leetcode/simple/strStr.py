# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/8 21:20
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:实现 strStr()
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""


def strStr(haystack, needle):
    len1 = len(haystack)
    len2 = len(needle)
    for i in range(len1 - len2 + 1):
        if haystack[i:i + len2] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))