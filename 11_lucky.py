#! /usr/bin/env python3
# 11_lucky.py - 对多个搜索关键字打开多个对应的网页，运用百度搜索引擎
import webbrowser, sys, bs4, requests


print('Searching...')
res = requests.get('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))      # 找到查询结果的链接
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

linkElems = soup.select('.t a')      # 查找CSS类t的元素中的<a>元素，即所得结果的超链接，阅读网页源码才能发现是t类

# 打开前5个关键字的查询结果
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))

