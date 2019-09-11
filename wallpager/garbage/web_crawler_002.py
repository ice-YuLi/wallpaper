# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import os
import random
import ctypes
import time


def url_info(target):
    req = requests.get(url=target)
    # 查看网址的编码
    # print(req.apparent_encoding)
    # req.encoding = 'GB2312'
    req.encoding = req.apparent_encoding
    html = req.text
    # 去标签
    bf = BeautifulSoup(html, "html.parser")
    bf.prettify()
    # html机构
    # print(bf.title)
    # print(type(bf.title))
    # print(bf.title.string)
    # print(bf.head)
    # print(bf.p)
    texts = bf.find_all('div', class_='list')
    print(type(texts))
    print(texts)
    root = 'E:\\text_lj\\'
    for item in texts:
        for item2 in item.find_all('li'):
            print(item2.img['src'])
            http_img = item2.img['src']
            url = http_img.split('/')[-1]
            path = root + url
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                else:
                    print('文件已存在')
                r = requests.get(http_img)
                r.raise_for_status()
                with open(path, 'wb') as f:
                    f.write(r.content)
                print('爬虫完成')
            except Exception as e:
                print('异常' + e)


    # 取图片
    # bf2 = BeautifulSoup(texts.decode('GB2312'), "html.parser")
    # texts2 = bf2.find_all('img')
    # print(texts2)


def tran_wall(path):
    while True:
        file = os.listdir(path)
        filepath = path + random.choice(file)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)  # 设置桌面壁纸
        time.sleep(0.1 * 60);


if __name__ == "__main__":
    # url_info('http://www.netbian.com/')
    tran_wall('E:\\test_lj\\')