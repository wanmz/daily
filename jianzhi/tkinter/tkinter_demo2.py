# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/18 0:28
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
from tkinter import *
from tkinter import ttk
from modules.reqs import *  # 导入reqs请求函数
import time
import random

# 创建窗体
root = Tk()
root.title('MyApp')
root.resizable(width=False, height=False)
root.config(background='#EEE')
root.geometry('500x240')

# 启动获取动作
def run():
    getAll(cookieStr)

# 信息的自刷新函数
def refreshInfo():
    info.config(text=genInfoStr())
    info.after(500, refreshInfo)

# ---创建界面
ttk.Frame(root, height=20).grid()
rown=0
# Cookie输入框
rown+=1
cookieStr = StringVar()
cookieStr.set('请在这里粘贴浏览器中的Cookie字段')
iptCookie = ttk.Entry(root, textvariable=cookieStr)
iptCookie.grid(
    row=rown, column=1, pady=10, padx=10, ipady=5, sticky='WE')

# 账户名输入框
rown+=1
nameStr=StringVar()
nameStr.set('请输入您的简书账户名')
iptName = ttk.Entry(root, textvariable=nameStr)
iptName.grid(
    row=rown, column=1, pady=10, padx=10, ipady=5, sticky='WE')

# 运行按钮
rown+=1
bt = ttk.Button(root, text='开始下载', width=30, command=run)
bt.grid(
    row=rown, column=1, padx=10, ipady=10, ipadx=10, sticky=E)

# 信息标签
rown+=1
info = ttk.Label(root, text='?/?')
info.grid(row=rown, column=1, padx=10, ipady=10, ipadx=10, sticky=E)
info.after(500, refreshInfo)  # 自动循环更新

root.mainloop()