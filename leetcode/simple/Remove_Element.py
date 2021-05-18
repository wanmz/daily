# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/3 20:21
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:移动元素
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""


def removeElement(nums, val):
    # i为不同元素的数组的长度
    i = 0
    for j in range(0, len(nums)):
        # 如果nums[j]不等于val, 则将nums[j]赋值给nums[i]即可, i自增
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == '__main__':
    # nums = [3, 2, 2, 3]
    # val = 3
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement(nums, val))