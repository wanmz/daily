# -*- coding:utf-8 -*-

# @Date         : 2021/2/19 7:43
# @Author       : wmzhong
# @Email        : 289241101@qq.com
# @description  : 整数反转


def reverse(x):
    s = str(x)
    if s[0] == '-':
        # 去掉第一个元素，然后做逆序，再转换成整整型
        x = int('-' + s[1:][::-1])
    else:
        x = int(s[::-1])
    return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    x = 120
    print(reverse(x))
