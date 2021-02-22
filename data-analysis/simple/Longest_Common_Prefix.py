# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/22 20:41
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:最长公共前缀
题目: https://leetcode-cn.com/problems/longest-common-prefix/
-------------------------------------------------
"""

def longstrComonPrefix(strs):
    s = ""
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    for i in zip(*strs):
        print(i)
        if len(set(i)) == 1:
            s += i[0]
        else:
            break
    return s


def longstrComonPrefix2(strs):
    if not strs: return ""
    str0 = min(strs)
    str1 = max(strs)
    for i in range(len(str0)):
        if str0[i] != str1[i]:
            return str0[:i]
    return str0


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    # print(longstrComonPrefix(strs))
    print(longstrComonPrefix2(strs))
