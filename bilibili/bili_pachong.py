import requests, csv, time
import sys
from bs4 import BeautifulSoup as BS

'''获取网页内容'''


def request_get_comment(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)',
               'Cookie': 'LIVE_BUVID=AUTO7215383727315695; stardustvideo=1; rpdid=kwxwwoiokwdoskqkmlspw; '
                         'fts=1540348439; sid=alz55zmj; CURRENT_FNVAL=16; _uuid=08E6859E-EB68-A6B3-5394-65272461BC6E49706infoc; '
                         'im_notify_type_64915445=0; UM_distinctid=1673553ca94c37-0491294d1a7e36-36664c08-144000-1673553ca956ac; '
                         'DedeUserID=64915445; DedeUserID__ckMd5=cc0f686b911c9f2d; SESSDATA=7af19f78%2C1545711896%2Cb812f4b1; '
                         'bili_jct=dc9a675a0d53e8761351d4fb763922d5; BANGUMI_SS_5852_REC=103088; '
                         'buvid3=AE1D37C0-553C-445A-9979-70927B6C493785514infoc; finger=edc6ecda; CURRENT_QUALITY=80; '
                         'bp_t_offset_64915445=199482032395569793; _dfcaptcha=44f6fd1eadc58f99515d2981faadba86'}

    response = requests.get(url=url, headers=headers)
    soup = BS(response.text.encode(response.encoding).decode('utf8'), 'lxml')
    result = soup.find_all('d')
    if len(result) == 0:
        return result
    all_list = []
    for item in result:
        barrage_list = item.get('p').split(",")
        barrage_list.append(item.string)
        barrage_list[4] = time.ctime(eval(barrage_list[4]))
        all_list.append(barrage_list)
    return all_list


'''最新弹幕文件'''


def get_new_barrage():
    for i in range(len(cid_list)):
        url = "https://comment.bilibili.com/%d.xml" % cid_list[i]
        url_list.append(url)
        file_name = "鬼灭之刃{}.csv".format(i + 1)
        with open(file_name, 'w', newline='', errors='ignore') as fd:
            comment = request_get_comment(url)
            writer = csv.writer(fd)
            writer.writerow(tableheader)
            if comment:
                for row in comment:
                    # print(row)
                    writer.writerow(row)
            del comment
        print('爬取完成！')


if __name__ == '__main__':
    url_list = []
    # 每一话的视频ID
    # cid_list = [125463156, 126679498, 87351529, 130657281, 130657521, 132024713,
    #             132024933, 134549763, 134547528, 134548247, 97118642, 134548562]
    # 知识区：213652346 数码区：214634486 游戏区：214506109 音乐区：213794602 动画区：213749562 鬼畜区：210738676 娱乐区：214632912
    # cid_list = [213652346, 214634486, 214506109, 213794602, 213749562, 210738676]
    cid_list = [136278570]
    tableheader = ['弹幕出现时间', '弹幕格式', '弹幕字体', '弹幕颜色', '弹幕时间戳',
                   '弹幕池', '用户ID', 'rowID', '弹幕信息']
    get_new_barrage()
