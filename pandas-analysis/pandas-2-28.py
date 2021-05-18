# -*- coding:utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/3/1 22:09
# @Author   :wmzhong
# @Email    :wmzhong_01@163.com
# @Bolg     :https://home.cnblogs.com/wmzhong
# @jianshu  :https://www.jianshu.com/u/2ef83f0891c7
# @Description:爬取网易云音乐数据
# @公众号    :Python与数据分析之美
-------------------------------------------------
"""
import re
import requests
from bs4 import BeautifulSoup


# 解析作者ID和名字
class Singer(object):
    def __init__(self):
        self.singer_url = "http://music.163.com/discover/artist/cat"
        self.singer_data = []
        self.singer_id = str()
        self.singer_name = str()

    def get_singer_html(self):
        res = requests.get(self.singer_url).text
        return res

    def del_singer_data(self, res):
        soup = BeautifulSoup(res, "html.parser")
        singer_id_name_list = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})
        for line in singer_id_name_list:
            # 每个作者对应一个ID
            self.singer_id = re.search(r"(\d+)", line.get('href')).group(0)
            # 每个作者名
            self.singer_name = line.get('title')[:-3]
            self.singer_data.append({"singer_id": self.singer_id, "singer_name": self.singer_name})
        return self.singer_data

    def run(self):
        res = self.get_singer_html()
        data = self.del_singer_data(res)
        return data


# 根据歌手ID或者专辑
class Album(object):
    def __init__(self):
        self.album_url = "http://music.163.com/artist/album?id="
        self.album_id = str()
        self.album_data = []
        self.album_name = str()

    def get_album_html(self, singer_id):
        url = self.album_url+singer_id
        res = requests.get(url).text
        return res

    def del_album_data(self, res):
        soup = BeautifulSoup(res, "html.parser")
        album_id_name_list = soup.find_all('a', attrs={'class': 'tit s-fc0'})
        for line in album_id_name_list:
            self.album_id = re.search(r"(\d+)", line.get('href')).group(0)
            self.album_name = line.get_text()
            self.album_data.append({"album_id": self.album_id, "album_name": self.album_name})
        return self.album_data

    def run(self, id):
        res = self.get_album_html(id)
        data = self.del_album_data(res)
        return data


# 获取歌曲信息
class Song(object):
    def __init__(self):
        self.song_url = "http://music.163.com/album?id="
        self.song_id = str()
        self.song_data = []
        self.song_name = str()

    def get_song_html(self, album_id):
        url = self.song_url+album_id
        res = requests.get(url).text
        return res

    def del_song_data(self, res):
        soup = BeautifulSoup(res, "html.parser")
        song_id_name_list = soup.find('ul', attrs={'class': 'f-hide'}).find_all('li')
        for line in song_id_name_list:
            music = line.find('a')
            # print(music)
            self.song_id = re.search(r"(\d+)", music.get('href')).group(0)
            self.song_name = music.get_text()
            self.song_data.append({"song_id": self.song_id, "song_name": self.song_name})
        return self.song_data

    def run(self, id):
        res = self.get_song_html(id)
        data = self.del_song_data(res)
        return data


# 每首歌的评论总数，及最火的评论对应作者，内容
class Comment(object):
    def __init__(self):
        self.song_url = "http://music.163.com/playlist?id="
        self.content_data = str()
        self.content_dict = dict()
        self.headers = {
            'Host': 'music.163.com',
            'Connection': 'keep-alive',
            'Content-Length': '484',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://music.163.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Cookie': 'JSESSIONID-WYYY=b66d89ed74ae9e94ead89b16e475556e763dd34f95e6ca357d06830a210abc7b685e82318b9d1d5b52ac4f4b9a55024c7a34024fddaee852404ed410933db994dcc0e398f61e670bfeea81105cbe098294e39ac566e1d5aa7232df741870ba1fe96e5cede8372ca587275d35c1a5d1b23a11e274a4c249afba03e20fa2dafb7a16eebdf6%3A1476373826753; _iuqxldmzr_=25; _ntes_nnid=7fa73e96706f26f3ada99abba6c4a6b2,1476372027128; _ntes_nuid=7fa73e96706f26f3ada99abba6c4a6b2; __utma=94650624.748605760.1476372027.1476372027.1476372027.1; __utmb=94650624.4.10.1476372027; __utmc=94650624; __utmz=94650624.1476372027.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        }
        self.params = {
            'csrf_token': ''
        }

        self.data = {
            'params': 'Ak2s0LoP1GRJYqE3XxJUZVYK9uPEXSTttmAS+8uVLnYRoUt/Xgqdrt/13nr6OYhi75QSTlQ9FcZaWElIwE+oz9qXAu87t2DHj6Auu+2yBJDr+arG+irBbjIvKJGfjgBac+kSm2ePwf4rfuHSKVgQu1cYMdqFVnB+ojBsWopHcexbvLylDIMPulPljAWK6MR8',
            'encSecKey': '8c85d1b6f53bfebaf5258d171f3526c06980cbcaf490d759eac82145ee27198297c152dd95e7ea0f08cfb7281588cdab305946e01b9d84f0b49700f9c2eb6eeced8624b16ce378bccd24341b1b5ad3d84ebd707dbbd18a4f01c2a007cd47de32f28ca395c9715afa134ed9ee321caa7f28ec82b94307d75144f6b5b134a9ce1a'
        }

    def get_comment_html(self, album_id):
        url = self.song_url+album_id
        self.headers['Referer'] = url
        res = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(album_id),
                            headers=self.headers, params=self.params, data=self.data).json()
        return res

    @staticmethod
    def del_comment_data(res):
        content_data = []
        hot_comments = res["hotComments"]
        for line in hot_comments:
            content_data.append({"user": line["user"]["nickname"],
                                 "content": line["content"],
                                 "like_count": line["likedCount"]})

        return res["total"], content_data

    def run(self, id):
        res = self.get_comment_html(id)
        total, data = self.del_comment_data(res)
        return total, data


if __name__ == '__main__':
    #
    singer = Singer()
    singer_data = singer.run()
    print(singer_data)
    album = Album()
    album_data = album.run("4292")
    print(album_data)
    song = Song()
    song_data = song.run("36784299")
    print(song_data)
    # 写多次循环获取评论的时候，最好不要以歌手为循环初始节点，否则容易造成404
    comment = Comment()
    comment.run("519250020")
