# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/17 22:59
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
# 实现窗口可视化
-------------------------------------------------
"""
import tkinter as tk


class GUI:
    def __init__(self, master):
        self.master = master
        self.face = tk.Frame(self.master, )
        self.face.pack()

        tk.Label(self.face, text='账户').pack()
        self.t_account = tk.Entry(self.face, )
        self.t_account.pack()

        tk.Label(self.face, text='密码').pack()
        self.t_password = tk.Entry(self.face, )
        self.t_password.pack()
        btn_login = tk.Button(self.face, text='login', command=self.login)
        btn_login.pack()

    def login(self):
        account = self.t_account.get()
        password = self.t_password.get()
        # 判空操作：略
        print(account, password)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('根据关键词搜索百度网址里邮箱信息')
    root.geometry('200x200')

    GUI(root)
    root.mainloop()