# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/24 21:15
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:有效的括号
# 出处:https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
-------------------------------------------------
"""
def isValid(s):
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1


if __name__ == '__main__':
    s = "()"
    print(isValid(s))

