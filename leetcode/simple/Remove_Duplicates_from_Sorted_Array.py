# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/25 19:59
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:删除排序数组中的重复项
# 参考:https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/python3-by-xilepeng-9/
-------------------------------------------------
"""

def removeDuplicates(nums):
    length = 0
    if len(nums) == 0: return length
    for i in range(1, len(nums)):
        if nums[length] < nums[i]:
            length += 1
            nums[length] = nums[i]
    return length + 1


if __name__ == '__main__':
    # nums = [1, 1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))