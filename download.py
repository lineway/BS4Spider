# coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import urllib
import sys
import time
# PATH = r'F:\download'

# 查看下载进度
def Schedule(a, b, c):
	per = 100.0 * a * b / c
	if per > 100:
		per = 100
	print '%.2f%%' % per
	# 控制下载速度
	time.sleep(.01)


try:
	URL = sys.argv[1]
	PATH = sys.argv[2]
except IndexError as e:
	print "请检查链接地址或存储路径."
else:
	filename = URL.split('/')[-1]
	addr = os.path.join(PATH, filename)
	urllib.urlretrieve(URL, addr, Schedule)
