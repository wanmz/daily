# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/20 19:56
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:罗马数字转整数
-------------------------------------------------
"""

def romanToInt(s):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
            ans -= a[s[i]]
        else:
            ans += a[s[i]]
    return ans


if __name__ == '__main__':
    # x = "III"
    x = "LVIII"
    print(romanToInt(x))


