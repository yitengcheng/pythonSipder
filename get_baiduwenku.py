#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


class BaiduWenku(object):
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
            image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/\
            537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'wenku.baidu.com',
            'Referer': 'https://wenku.baidu.com/search?word=2018%C4%EA%B1%A6%B1\
            %A6%CA%B2%C3%B4%C3%FC&lm=0&od=0&fr=top_home&ie=gbk',
            'Upgrade-Insecure-Requests': '1',
        }
        self.file = open('/Users/smt/Desktop/baiduTest.txt', 'a+')

    def spider(self, html):
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all('div')
            print(divs)
            # for p in divs:
            #     p.find_all('p'):
            #         if p == '&nsp;':
            #             self.file.write('\n')
            #         else:
            #         self.file.write(p.get_text())

    def craw(self, url):
            r = requests.get(url, self.headers)
            r.encoding = 'gb2312'
            self.spider(r.text)

if __name__ == '__main__':
    obj_spider = BaiduWenku()
    # url = input('请输入网址')
    obj_spider.craw('https://wenku.baidu.com/view/a24d12c7bb0d4a7302768e9951e79\
        b8968026883.html?from=search')
