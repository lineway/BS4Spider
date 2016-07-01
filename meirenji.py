# coding:utf-8
from bs4 import BeautifulSoup
import requests
import time

url_list_one = []
headers = {
"Cookie": "firstentry=%2Fpost.do%3FloftBlogName%3Dloftermeirenzhi%26loftPostUrl%3D1d09be09_b85298c%26X-From-ISP%3D2|; usertrack=c+xxC1d2NRPDSjBpDMgoAg==; NTESLOFTSI=EB3EA3726EAB0D93738F5A7AAF9B8DE3.classa-lofter6-8010; JSESSIONID-WLF-XXD=f78af58db6a2fddb5ae2e87ee4a4f1b7a636647da6b3eda8efe148c040759ca76ed06b4f01f3445478c11b1b9715946d0b49e2be65cb0c0ef4cc55d737821f29df7d0e032ef4050153ff14bda59dbea3df7b3c20c4196f288647ded501e2472366c16e91bd2eae4a902db537f1a15d3995d2d34c0939dbe7c9dd91a3d14467d86923b4e8; _ntes_nnid=badf16f80a418934ca93444c0e083fbd,1467364639721; _gat=1; _ga=GA1.2.2144800920.1467364640; fastestuploadproxydomainkey=uploadbj|1467364649191; reglogin_hasopened=1; reglogin_isLoginFlag=; regtoken=1000; NTES_SESS=mXoEeis42iUpavk7mSHMzgo.AoNmCSHVMd4vA05IUhsIvf1AAjt3ZUMyIkw37fTq3VOjk99rbNAcokIAcxsCiWrDtyS.gDf1_s18mx18Bz.sNQmbPoPx.EQDyAqLGZ8okTaseoY_PJxuT.yP8CacIvwzrQKkFxBl4J0Na_7ykbLTTgCf8CQULoqBD6TSzoDf4; NTES_PASSPORT=ErFf6BEh4FXsyQbRzhlNy.THrqpYzzgTTwvlz86axPW6HOV44lop96f7Tt3pzOFUptSoIjtxUZmlQW3cvrIL_bkY5H86l...D5NhWtmIuddl7; S_INFO=1467364726|0|3&100#1&25#3&100|zhangyiming07; P_INFO=zhangyiming07@163.com|1467364726|1|lofter|11&14|bej&1467268017&lofter#bej&null#10#0#0|187121&0|lofter|zhangyiming07@163.com; noAdvancedBrowser=0; __utma=61349937.2144800920.1467364640.1467364640.1467364640.1; __utmb=61349937.10.7.1467364649098; __utmc=61349937; __utmz=61349937.1467364640.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
}
path = '/Users/zhangyiming/Downloads/Image/'
url_host = ["http://loftermeirenzhi.lofter.com/?page={}".format(str(i)) for i in range(1,78)]
for url in url_host:
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('div.pic a')
    for link in links:
        clean_url = link.get('href')
        print clean_url
        url_list_one.append(clean_url)

        for son_url in url_list_one:
            web_data = requests.get(son_url)
            image_urls = soup.select('div.pic img')
            for image_url in image_urls:
                image_list_one = []
                url_need = image_url.get('src').split('?')[0]
                r = requests.get(url_need)
                with open(path+url_need[-15:], 'wb') as jpg:
                    jpg.write(r.content)
                #     image_list_one.append(url_need)
                # else:
                #     image_list_one.append(image_url)
                #     print image_list_one



    # for image_url in url_List:
    #     web_data = requests.get(image_url, headers=headers)
    #     soup = BeautifulSoup(web_data.text, 'lxml')
    #     image_links = soup.select('div.pic img')
        # for image_link in image_links:
        #     url_1 = image_link.get('src')
        #     url_2 = url_1.split("?")[0]
        #     url_List.append(url_2)
        #     for i in url_List:
        #         j = requests.get(i)
        #         with open(path+i[-15:], 'wb') as jpg:
        #             jpg.write(j.content)
            # image_addr = image_link.get('src')
            # with open(path+image_addr[-15:0], 'wb') as jpg:
            #     jpg.write(image_addr.content)
