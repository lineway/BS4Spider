# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib
from multiprocessing import Pool

MAINURL = "http://www.maiziedu.com/course/331/"
CUMURL = "http://www.maiziedu.com/"
NEEDURL = []
DOWNLOADURL = []
TITLE = []
PATH = r"H:\video\MysqlBase"

def get_real_video(mainurl):
    web_data = requests.get(mainurl)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    name_tag = soup.select('body > div.video-lists-container.vlesson-info > div.fl.vlesson-infoR > h1')
    name = name_tag[0].get_text()
    h2url = soup.select('body > div.video-lists-container.marginB40 > div.VLCleft > div > div > ul')
    title = h2url[0].get_text()
    for short_url in h2url[0].find_all('a'):
        real_url = str(CUMURL) + short_url.get('href')
        NEEDURL.append(real_url)
    for video_url in NEEDURL:
        web_data = requests.get(video_url)
        soup = BeautifulSoup(web_data.text, 'lxml')
        title_tag = soup.select('body > div.video > div.play_panel > div > div > div.bottom-module > span')
        title = title_tag[0].get_text()
        TITLE.append(title)
        js_script = soup.select("head > script")
        scripts = js_script[0]
        for script in scripts:
            # print script
            strings = script.split(',')
            download_url = strings[-1].strip().split('"')[1]
            DOWNLOADURL.append(download_url)
    for filename, download in zip(TITLE, DOWNLOADURL):
        addr = os.path.join(PATH, filename + '.mp4')
        urllib.urlretrieve(download, addr, Schedule)


def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

if __name__ == '__main__':
    get_real_video(MAINURL)
