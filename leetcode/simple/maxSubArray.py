# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/13 11:46
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:最大子序和
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""


def maxSubArray(nums):
    tmp = nums[0]
    max_ = tmp
    n = len(nums)
    for i in range(1, n):
        # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
        if tmp + nums[i] > nums[i]:
            max_ = max(max_, tmp + nums[i])
            tmp = tmp + nums[i]
        else:
            # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
            max_ = max(max_, tmp, tmp + nums[i], nums[i])
            tmp = nums[i]
    return max_


if __name__ == '__main__':
    # nums = [1]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))