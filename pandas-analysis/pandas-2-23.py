# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/2/23 20:53
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
-------------------------------------------------
"""
import numpy as np
import pandas as pd

# path = "C:/Users/Administrator/Downloads/2021年员工春节礼品邮寄地址收集-云服务业务部.xls"

# df = pd.read_excel(path)

# 获取某列最大值
# print(df['员工编码'].max())
# 某列最小值
# print(df['员工编码'].min())
# 某列中最大值位置
# print(df['员工编码'].argmax())
# 获取中位数
# print(df['员工编码'].median())

# 查看维度信息
# print(df.shape)
"""iloc获取具体参数信息，也可以通过loc"""
# 查看第四行
# print(df.iloc[4])
# 横着展示第四行
# print(df.iloc[[4]])
# 前两行
# print(df.iloc[[0, 1]])
# 获取坐标数据,[0,1]
# print(df.iloc[0, 1])
# 展示偶数行
# print(df.iloc[lambda x: x.index % 2 == 0])
# 获取第一行到第三行的第一列和第三列数据
# print(df.iloc[[0, 2], [1, 3]])
# 获取第一行到第三行的第一列到第三列数据
# print(df.iloc[1:3, 0:3])
# 展示所有行，获取第一列和第三列数据
# print(df.iloc[:, lambda df: [0, 2]])
# print(df.iloc[:, [0, 2]])

""" 排序问题"""
# by通过什么排序，支持字符或列表字符串
# axis=0 列排序， axis=1 索引排序
# ascending 排序，默认升序，True
# print(df.sort_values(by=["员工编码"], axis=0, ascending=False))

# na_position 支持{‘first’, ‘last’}，默认last, 把空值放最前还是最后
# print(df.sort_values(by=["收件人姓名"], axis=0, na_position='first'))
# print(df.sort_values(by=["员工编码"], axis=0, ascending=False).iloc[:8, :])

# 对员工编码这列数据，统计个数，并对索引列排序。
# print(pd.value_counts(df["员工编码"], sort=True).sort_index())

# 数据统计，最大值、最小值、平均值、中位值、四分位值、标准差等。
# print(df.describe())
# 针对数字列做数据统计
# print(df.describe(include=[np.number]))
# 对指定列中数据做数据统计。
# print(df["员工编码"].describe(include=[np.number]))

"""数据集成: merge，concat, combine_first三个参数还需继续看。"""

"""字符串处理 pandas.Series.str.extract"""
# 对某列字符串捞取数字值
# print(df["收件人详细地址"].str.extract('(\d+)'))
# expand=True返回DataFrame，expand=False返回Series
# print(df["收件人详细地址"].str.extract('(\d+)', expand=True))
# 针对某列值字符串，按特定符号分割。
# df['现价']=df['现价'].str.split('-', expand=True)[0]

"""数据类型处理"""
# 对时间做格式化。
# df['当前时间']=pd.to_datetime(df['当前时间'],format='%Y%m%d')

# 将时间序列设置为索引并按照索引进行排序
# data=df.set_index(df['当前时间']).sort_index()

# 由于月销量数据带有字符串，所以需要将字符串替换，并最终转化为数值型
# data['月销量']=data['月销量'].str.replace('万','0000')
# data['月销量']=data['月销量'].str.replace('+','')
# data['月销量']=data['月销量'].str.replace('.','').astype(np.float64) 字符串类型转换

"""缺省值处理"""
# 查找缺失值，看那些列存在缺失值, any()某一列出现空值, all()所有列都是空值
# print(df.isnull().any())
# print(df.isnull().all())
# 筛选出任何含有缺失值的数据
# print(df.isnull().values==True)
# print(df.isnull().any().values==True)
# 统计某一列缺失值的数量
# print(df["收件省"].isnull().value_counts())
# print(df["收件省"].isnull().values==True)

"""删除缺省值"""
# subset和thresh参数来删除你需要删除的缺失值，inplace则表示是否在原表上替代
# print(df.dropna(axis=0, subset=["收件省"]))

filepath = r'F:\analysis-study-data\eg1.xls'
df = pd.read_excel(filepath)
# 某列求平均值
# print(df["数量"].mean())
# 利用某列均值来对NA值进行填充
# print(df["数量"].fillna(df["数量"].mean()))
# 利用某列中位数来对NA值进行填充
# print(df["数量"].fillna(df["数量"].median()))

"""重复值处理"""
# duplicated找出重复值,不加subset默认所有列,keep=first 第一次重复列标记为True
# print(df.duplicated(subset=["效期"], keep='first'))
# 除了最后出现的情况外，将重复项标记为True。
# print(df.duplicated(subset=["效期"], keep='last'))

# 删除"效期"列存在重复的行数据。
# print(df.drop_duplicates(subset=["效期"], keep='first', inplace=False))

# drop 删除多余行或列

"""数据变换"""
# 由于“累计评价”的值太大，我们新增一列对“累计评价”取对数处理
# data['对数_累计评价']=np.sqrt(data['累计评价'])

#插入一列，计算“优惠力度”
# data['优惠力度']=data1['现价']/data1['原价']

"""数据精简"""
#随机不重复抽取100行数据样本
# data.sample(n=100)

# 分组求和
# data.groupby(by='店铺名称')['月销量'].sum()

