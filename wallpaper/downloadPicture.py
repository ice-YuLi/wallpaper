# encoding: utf-8
import requests
import json
import random
import os, sys
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import ctypes
from readconfig import readconfig


def get_url1(options):
    search_url = 'https://unsplash.com/napi/search?client_id=%s&query=%s&page=1'
    client_id = 'fa60305aa82e74134cabc7093ef54c8e2c370c47e73152f72371c828daedfcd7'
    categories = ['nature', 'flowers', 'wallpaper', 'landscape', 'sky']
    if len(options) > 0:
        categories = options
    option = random.choice(categories)
    print(option)
    search_url = search_url % (client_id, option)
    response = requests.get(search_url)

    data = json.loads(response.text)
    results = data['photos']['results']
    # results = list(filter(lambda x: float(x['width']) / x['height'] >= 1.33, results))
    result = random.choice(results)
    result_id = str(result['id'])
    result_url = result['urls']['regular']

    return result_id, result_url


error_count = 0


def get_url2(options):
    global error_count
    id_name = 'error'
    pic_url = 'https://up.enterdesk.com/edpic_source/a3/4a/09/a34a09feec74ad2c4452a20f3ef39421.jpg'
    if error_count > 5:
        ctypes.windll.user32.MessageBoxW(0, '别试了，错了就是错了，告诉我一声吧！', '更换壁纸', 0)
        sys.exit()
    try:
        search_url = 'https://www.enterdesk.com/zhuomianbizhi/%s'
        categories = ['fengjing', 'huahui', 'renwenbizhi', 'qichebizhi', 'yingshibizhi', 'mingxingbizhi', 'meishibizhi', 'sheying']
        if len(options) > 0:
            categories = options
        option = random.choice(categories)
        search_url = search_url % option
        # print(search_url)
        # 第一步
        response = requests.get(search_url)
        response.encoding = response.apparent_encoding
        html = response.text
        bf = BeautifulSoup(html, "html.parser")
        bf.prettify()
        texts = bf.find_all('a', class_='wrap no_a')
        for item in texts:
            url_str = item.attrs['href']
        str_find1 = url_str.rfind('.html')
        if str_find1 == -1:
            ctypes.windll.user32.MessageBoxW(0, '设置设置失败，为什么啊！！！', '右键快捷菜单设置（更换壁纸）', 0)
            sys.exit()
        str_find2 = url_str.rfind('/')
        total = url_str[str_find2 + 1: str_find1]
        random_page = random.randint(1, int(total))
        search_url = search_url + '/' + str(random_page) + '.html'
        # 第二步
        req = requests.get(search_url)
        req.encoding = req.apparent_encoding
        bf = BeautifulSoup(req.text, "html.parser")
        texts = bf.find_all('div', class_='egeli_pic_li')
        option = random.choice(texts)
        pic_url = option.find_all('a')[0].attrs['href']
        # 第三步
        req = requests.get(pic_url)
        req.encoding = req.apparent_encoding
        bf = BeautifulSoup(req.text, "html.parser")
        texts = bf.find_all('img', attrs={'class': 'arc_main_pic_img'})
        pic_url = texts[0].attrs['src']
        # print(pic_url)
        # 第四步
        id_name = pic_url[pic_url.rindex('/') + 1:pic_url.rindex('.')]
        error_count = 0
    except Exception as e:
        get_url2(options)
        error_count += 1
    return id_name, pic_url


def download_picture():
    root = 'D:\\wallpaper\\'
    # 根据配置文件自定义配置
    address, options = readconfig()
    id, url = eval(address + '(' + options + ')')
    if not os.path.exists(root):
        os.mkdir(root)
    jpg_file = root + id + '.jpg'
    r = requests.get(url)
    r.raise_for_status()
    with open(jpg_file, 'wb') as file:
        file.write(r.content)

    return jpg_file


if __name__ == "__main__":
    download_picture()
    # pyinstaller -w -F -i blueWhaleLogo15.ico wallpaper.py

