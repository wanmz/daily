# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/16 18:26
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Description:
  通过百度搜索关键词拿下来连接去访问网站获取下方邮箱。
-------------------------------------------------
"""
import re
import json
import time
import random
import requests
import xlwt
from bs4 import BeautifulSoup
from urllib import parse
import tkinter as tk
from tkinter import messagebox


UA = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0;\
       Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1))',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; 360SE)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
      'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 \
      (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) \
      Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; \
      .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; \
      .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',

      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) \
      Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0',

      'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) \
      Version/5.0.2 Mobile/8C148 Safari/6533.18.5',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)']


def print_book_lists_excel(book_lists, sheet_name):
    filename = "%s.xls" % sheet_name
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, len(book_lists)):
        for j in range(0, len(book_lists[i])):
            sheet.write(i, j, book_lists[i][j])
    workbook.save(filename)


class GUI:
    def __init__(self, master):
        self.master = master
        self.face = tk.Frame(self.master, )
        self.face.pack()

        tk.Label(self.face, text='关键词').pack()
        self.t_password = tk.Entry(self.face, )
        self.t_password.pack()
        btn_login = tk.Button(self.face, text='开始搜索', command=self.login)
        btn_login.pack()

    def login(self):
        cnt = 1
        res_data = []
        password = self.t_password.get()
        # 判空操作：略
        print("关键词 " + password)
        res_data.append(['标题', '网址', '邮箱'])
        # page = 1
        if len(password) < 1:
            tk.messagebox.showerror('Error', "请输入关键词")
            exit(0)
        keyword = parse.quote(password)
        for page in range(0, 1):
            # 增加重连次数
            requests.adapters.DEFAULT_RETRIES = 5
            # 关闭多余连接
            # s = requests.session()
            # s.keep_alive = False
            url = "https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=BCD0B91E1D317479&ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd={}&pn={}&rsv_spt=1&oq={}&rsv_pq=84e14ff2001000e6&rsv_t=04590DHGV1cx8hddnxctMrl22mcD1W%2BoLPJG1u8EW%2FJW217wLTbG749noPOQRILb3sSG&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs={}&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=0&_cr1=38785"\
                .format(keyword, page*10, keyword, keyword)
            # print(url)
            # 测试
            # url = "https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=BEF5B21C8F360107&ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=%E5%9C%A8%E7%BA%BF%E8%A7%82%E7%9C%8B&rsv_spt=1&oq=%25E5%259C%25A8%25E7%25BA%25BF%25E8%25A7%2582%25E7%259C%258B&rsv_pq=a806fce900131b2a&rsv_t=0987aRlwHz8UpcepFFOEKrH0ZlEoibTZ8WO3%2BeMRQHIF5vMoJ5q7TN%2FeW0NkhUObgR2V&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs=%E5%9C%A8%E7%BA%BF%E8%A7%82%E7%9C%8B&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=0&_cr1=33627"
            cookie = "BIDUPSID=BCD0B94E9998FE24710B8204F8BC4C43; PSTM=1602896500; BD_UPN=12314753; BDUSS=3VtamJ5T1hNWlNYam5ObC1-T0tTWk51Z01lNml3S1VINS1HTXUtemtiRjJhRmxnSVFBQUFBJCQAAAAAAAAAAAEAAABzSTMVbWluZ3pob25nMDEyMzQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHbbMWB22zFgd; BDUSS_BFESS=3VtamJ5T1hNWlNYam5ObC1-T0tTWk51Z01lNml3S1VINS1HTXUtemtiRjJhRmxnSVFBQUFBJCQAAAAAAAAAAAEAAABzSTMVbWluZ3pob25nMDEyMzQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHbbMWB22zFgd; MCITY=-:; __yjs_duid=1_eb6b424c44a6d8fa791ade34ea4993181620214096257; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=BEF5B2B7397E634C6D14E92405D1C8F3:FG=1; H_PS_PSSID=33801_33967_31660_34004_33676_33607_33909_26350; BDSFRCVID=laKOJeC62m0UgAjeCRKXdFAdrZGrtPJTH6aoVKvBtVxiBxoW3RhuEG0Psx8g0KubRVd0ogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbuJ_D--tDK3J-ndbjK_2bk-hpoBaC62aKDs_-ncBhcqEIL4etJ-3-_XbtbNaT5b3e6bQq0-LR5RhUbSj4Qo5P_V3PKjyMnXMDr7VIOPyp5nhMJO3j7JDMP0-4bOtqJy523ion6vQpnljpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTjBjHuftTKsMDJaXCP8MncSJ-0kh4oMeP015-nZKxtqtjIj2hbVKJ5TVRnkbMjNbbDDQND85ljnWncKWMJc2K5zsU3EQfoDMRLPLJr405OTB5-O0KJcbRoSSqTvhPJvyT8DXnO7L4nlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtIFtVD8-JDKBMI-Cen6S-Rcbql7B2nvfHDo-LIv82qbcOR5Jj65hDM4vDHj-3hj3KKnl5Rb-aRTVOMoF3MA--t4QKnQ0at5uKa6w2bcaWljZsq0x0MnWe-bQypoa2pQAaKOMahkMal7xOM5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjTyDGtjtTDJfn38L5ryMPTofJcYq4bohjPT5-r9BtQmJJuq-pQgK4QqEUooqtOPLt0Xhfrvb4naQg-q3R7CWn5JsDok-U6RhpbL3HtO0x-jLT7OVn0MW-5DDh3yM-nJyUnQhtnnBpQW3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CFbtKtWhCtRejRbMt6H-pJW--QX5ICX3b7EfbRHOp7_bf--D4rQ3fJCatQmLe3v0pQp5PoAsPom0M6xy5K_hnji-fjJQjb05tnOQKOCj-5HQT3mKnvbbN3i-4jNQDPjWb3cWKJV8UbS3tRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50exbH55uttnAjoMK; BDSFRCVID_BFESS=laKOJeC62m0UgAjeCRKXdFAdrZGrtPJTH6aoVKvBtVxiBxoW3RhuEG0Psx8g0KubRVd0ogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbuJ_D--tDK3J-ndbjK_2bk-hpoBaC62aKDs_-ncBhcqEIL4etJ-3-_XbtbNaT5b3e6bQq0-LR5RhUbSj4Qo5P_V3PKjyMnXMDr7VIOPyp5nhMJO3j7JDMP0-4bOtqJy523ion6vQpnljpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTjBjHuftTKsMDJaXCP8MncSJ-0kh4oMeP015-nZKxtqtjIj2hbVKJ5TVRnkbMjNbbDDQND85ljnWncKWMJc2K5zsU3EQfoDMRLPLJr405OTB5-O0KJcbRoSSqTvhPJvyT8DXnO7L4nlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtIFtVD8-JDKBMI-Cen6S-Rcbql7B2nvfHDo-LIv82qbcOR5Jj65hDM4vDHj-3hj3KKnl5Rb-aRTVOMoF3MA--t4QKnQ0at5uKa6w2bcaWljZsq0x0MnWe-bQypoa2pQAaKOMahkMal7xOM5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjTyDGtjtTDJfn38L5ryMPTofJcYq4bohjPT5-r9BtQmJJuq-pQgK4QqEUooqtOPLt0Xhfrvb4naQg-q3R7CWn5JsDok-U6RhpbL3HtO0x-jLT7OVn0MW-5DDh3yM-nJyUnQhtnnBpQW3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CFbtKtWhCtRejRbMt6H-pJW--QX5ICX3b7EfbRHOp7_bf--D4rQ3fJCatQmLe3v0pQp5PoAsPom0M6xy5K_hnji-fjJQjb05tnOQKOCj-5HQT3mKnvbbN3i-4jNQDPjWb3cWKJV8UbS3tRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50exbH55uttnAjoMK; ab_sr=1.0.0_YTQyZjZlMzY4YmE4MDk0NTZiZGEwMDI3ZTVjNjI5Y2ZmODJiNWZmMWYyNjc5NTQwNDEyMGU3MTIzNDhiN2FmMWEzMDA5N2FkN2QzODJiNjdhMDJiMmRlODE5OWYyYzYx; H_PS_645EC=0987aRlwHz8UpcepFFOEKrH0ZlEoibTZ8WO3+eMRQHIF5vMoJ5q7TN/eW0NkhUObgR2V; WWW_ST=1621254353022"
            res = requests.get(url, headers={'User-Agent': UA[random.randint(0, len(UA) - 1)], 'cookie':cookie}).text
            i_soup = BeautifulSoup(res, "html.parser")
            div_list = i_soup.findAll('div', class_='c-tools c-gap-left')
            for line in div_list:
                time.sleep(5)
                data_tools = json.loads(line.get("data-tools"))
                title = data_tools["title"]
                line_url = data_tools["url"]
                # 测试地址
                # line_url = "http://www.mafengwo.cn/travel-news/220037.html"
                # print("抓取开始,实际请求Url:{0}, 标题:{1}".format(title, line_url))
                try:
                    res = requests.get(line_url, headers={'User-Agent': UA[random.randint(0, len(UA) - 1)]})
                    # 增加重连次数
                    s = requests.session()
                    # 关闭多余连接
                    s.keep_alive = False

                    # 处理网址重定向问题
                    print(res.url)
                    if res.url != line_url:
                        print("网址发生重定向")
                        line_url = res.url
                        res = requests.get(line_url, headers={'User-Agent': UA[random.randint(0, len(UA) - 1)]})
                except requests.exceptions.ConnectionError:
                    res.status_code = "Connection refused"
                if res.status_code != 200:
                    print("[%s]网站不可达, 跳过" % line_url)
                    continue
                res.encoding = 'utf8'
                # print(line_url)
                # print(res.text)
                # 正则表达式匹配邮箱
                try:
                    # mail = re.findall(r'[a-z_\-\.0-9]+@[a-z\-\.]+', res.text, re.DOTALL)
                    mail = re.findall(r'[a-z_\-\.0-9]+@[a-z]+\.[a-z0-9]+', res.text, re.DOTALL)
                except:
                    continue
                # print(mail)
                res_data.append([title, line_url, ','.join(mail)])
                print("获取第%s数据完成！！！" % cnt)
                cnt += 1
            # print(res_data)
            # debug测试
            # res_data = [['电影在线观看,电影免费下载,最新电视剧免费收看_唯美影视', 'http://www.baidu.com/link?url=eyoO4EhWzZ47TLmA2SYC5d_fAH4mDlPDrZ2Fts4D5fe', [], 200], ['胡巴鹿电影网-好看的电影电视剧免费在线观看-2020豆瓣高分电影推荐', 'http://www.baidu.com/link?url=VAPhmsYRjWks69QWGjRuDiOpoToy-w3FCx10bJZsrfy', ['huizisa@gmail.com'], 200], ['小马电影网-免费电影在线观看-好看的电视剧大全推荐', 'http://www.baidu.com/link?url=OP8Rwz5p6WqYtpromBGWEkgaPF0hf58vnSXVHTyPaDi', [], 200], ['恐怖影院-恐怖,僵尸,鬼片,手机电影在线观看', 'http://www.baidu.com/link?url=m5DoSDtYy3f4gQKvB_jSx_cUjlTek0TNwOCZjDM8I5zKTK6sU_d3pXGgDjSNRXRQ', [], 200], ['日剧网-最新韩剧,日剧,泰剧在线观看,热播韩剧网,韩剧TV网', 'http://www.baidu.com/link?url=neNj7OKE8KziY-M27Nnt4vplO3QcUf_GRTykqoowjeW', [], 200], ['【电视剧大全】_2021更新更好看的电视剧在线观看-2345电视剧', 'http://www.baidu.com/link?url=nGXBOzu5-d8WSSQmhyG5bGAo3uhFmXDRRz9wokI_dnW', [], 200], ['二三四五【影视大全】_2021影视大全在线观看', 'http://www.baidu.com/link?url=P3RqBZYRQK1ufC2urUCdjonPCwAvOOrVIsiEaiPnIUS', [], 200], ['电影网_1905.com', 'http://www.baidu.com/link?url=mvE1F6b2h-mUS6A2nVwnRvg8UFImasuGHFwUbZpl367', [], 200]]
        print_book_lists_excel(res_data, password)
        tk.messagebox.showinfo('Info', "下载完成！")


if __name__ == '__main__':
    root = tk.Tk()
    root.title('根据关键词搜索百度网址里邮箱信息')
    root.geometry('500x240')

    GUI(root)
    root.mainloop()
