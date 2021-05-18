# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/4 20:49
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:解析智联数据
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json(r'C:\Users\Administrator\Desktop\Python_全国JSON.json')
df.info()

df.index = df['ZL_Job_id']
del(df["ZL_Job_id"])
df_sort = df.sort_index()
df=df_sort
# df[['工作地点', '职位月薪']].head(10)


df['bottom'] = df['top'] = df['average'] = df['职位月薪']
pattern = re.compile('([0-9]+)')
q1=q2=q3=q4=0

for i in range(len(df['职位月薪'])):
    item = df['职位月薪'].iloc[i].strip()
    result = re.findall(pattern,item)
    try:
        if result:
            try:
            #此语句执行成功则表示result[0],result[1]都存在，即职位月薪形如‘6000-8000元/月’
                df['bottom'].iloc[i],df['top'].iloc[i] = result[0],result[1]
                df['average'].iloc[i] = str((int(result[0])+int(result[1]))/2)
                q1+=1

            except:
            #此语句执行成功则表示result[0]存在，result[1]不存在，职位月薪形如‘10000元/月以下’
                df['bottom'].iloc[i] = df['top'].iloc[i] = result[0]
                df['average'].iloc[i] = str((int(result[0])+int(result[0]))/2)
                q2+=1
        else:
        #此语句执行成功则表示【职位月薪】中并无数字形式存在，可能是‘面议’、‘found no element’
            df['bottom'].iloc[i] = df['top'].iloc[i] = df['average'].iloc[i] = item
            q3+=1

    except Exception as e:
        q4+=1
        print(q4,item,repr(e))

for i in range(100):#测试一下看看职位月薪和bottom、top是否对的上号
    print(df.iloc[i][['职位月薪','bottom','top','average']])#或者df[['职位月薪','bottom','top','average']].iloc[i]也可

df[['职位月薪','bottom','top','average']].head(10)

df['工作城市'] = df['工作地点']
pattern2 = re.compile('(.*?)(\-)')
df_city = df['工作地点'].copy()

for i in range(len(df_city)):
    item = df_city.iloc[i].strip()
    result = re.search(pattern2,item)
    if result:
        print(result.group(1).strip())
        df_city.iloc[i] = result.group(1).strip()
    else:
        print(item.strip())
        df_city.iloc[i] = item.strip()

df['工作城市'] = df_city
df[['工作地点','工作城市']].head(20)




