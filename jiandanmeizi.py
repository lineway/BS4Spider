# coding:utf-8
import requests
from bs4 import BeautifulSoup


# 保存文件夹路径
path = 'F:/image/'
urls = ['http://jandan.net/ooxx/page-{}#comments'.format(str(i)) for i in range(1985, 1500, -1)]
# headers数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Cookie': '660641210=8689Bhb9JVUbOaEjfCyeUn5we2WgHOZb85v1%2BJUN; _gat=1; 660641210=9a4akE95i7aILQywr9BEMnnXt6kW%2FvILQ%2FBQnLvs; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1463036794074; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1463036497; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1463036794; _ga=GA1.2.1365690603.1463036497',
}
img_url = []

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    img = soup.select('a.view_img_link')
    for i in img:
        z = i.get('href')
        if str('gif') in str(z):
            pass
        else:
            img_url.append(z)
    for i in img_url:
        r = requests.get(i)
        with open(path+i[-15:], 'wb') as jpg:
            jpg.write(r.content)
    print img_url


def download():
    for i in urls:
        get_info(i)
        img_url = []


download()
