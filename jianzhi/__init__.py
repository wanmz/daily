# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/16 18:22
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re

str = "联系方式：010-85550578"

# mail = re.findall(r'0\d{2,3}-\d{6,7,8}-[0-9]{0,4}', str, re.DOTALL)
mail = re.findall(r'[0][0-9]{2,3}-[0-9]{5,10}[\-0-9]{0,5}', str)
print(mail)