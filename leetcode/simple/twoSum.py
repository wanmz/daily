# -*- coding:utf-8 -*-

# @Date         : 2021/2/18 19:19
# @Author       : wmzhong
# @Email        : 289241101@qq.com
# @description  :


def twosum(nums, target):
    sdict = {}
    for ind, num in enumerate(nums):
        sdict[num] = ind
    for i, num in enumerate(nums):
        j = sdict.get(target - num)
        if j is not None and i != j:
            return [i, j]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twosum(nums, target))


