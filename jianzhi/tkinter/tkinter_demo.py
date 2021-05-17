# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/17 23:39
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:
# @公众号    :Python与数据分析之美
连接：https://blog.csdn.net/yeshankuangrenaaaaa/article/details/85704134
实现tkinter的密码验证,与数据库验证
-------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox
import sys
import pymysql


class loginf():
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

    def login(self, ):

        account = self.t_account.get()
        password = self.t_password.get()
        # 判空操作：略
        print(account, password)

        # 数据库处理
        connection = pymysql.connect(host='localhost', user='root', port=3306)
        try:
            with connection.cursor() as cursor:
                command1 = "use password;"
                command2 = "select password from passbook where account = (%s);"
                cursor.execute(command1)
                result = cursor.execute(command2, (account))

            connection.close()

        except:
            sys.exit()

        else:
            if result == 0:
                print('no this account!')
                tk.messagebox.showerror('Info', "Account Not Exist！")
            else:
                print('查找结果：', result)
                if cursor.fetchone()[0] == password:
                    print('Login successfully！')
                    tk.messagebox.showinfo('Info', "Login successfully！")
                    # 销毁登陆界面，生成登陆后界面
                    self.face.destroy()
                    homef(self.master)

                else:
                    print('password input error')
                    tk.messagebox.showerror('Info', "Password Error！")


class homef():
    def __init__(self, master):
        self.master = master
        self.face = tk.Frame(self.master, )
        self.face.pack()
        btn_showinfo = tk.Button(self.face, text='info', command=self.showinfo)
        btn_showinfo.pack()

    def showinfo(self, ):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Login with password')
    root.geometry('200x200')

    loginf(root)