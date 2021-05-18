# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/13 11:35
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:搜索插入位置
# @公众号    :Python与数据分析之美
# leetcode:https://leetcode-cn.com/problems/search-insert-position/solution/owende-di-liu-ti-by-vvi2ardly-jennings-ec8t/
-------------------------------------------------
"""

def searchInsert(nums, target):
    i = 0
    lens = len(nums)
    while nums[i] < target:
        i += 1
        if i == lens:
            return lens
    return i


if __name__ == '__main__':
    nums = [1,3,5,6]
    # target = 5
    target = 2
    print(searchInsert(nums, target))