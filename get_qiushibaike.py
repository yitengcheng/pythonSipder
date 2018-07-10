#!/usr/bin/env python3
## -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


class Qiushi(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        self.baseUrl = 'https://www.qiushibaike.com'
        self.spilUrl = 'https://www.qiushibaike.com/8hr/page/'
        self.file = open('/Users/smt/Desktop/test.txt', 'a+')

    def spider(self, html):
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all('div', re.compile('^article'))
            for div in divs:
                if div.find_all('div','thumb'):
                    continue
                elif div.find_all('div', 'content'):
                    self.file.write(div.span.get_text())
                    self.file.write('-----------------')

    def craw(self):
        for i in range(5):
            if i == 0:
                r = requests.get(self.baseUrl, self.headers)
                self.spider(r.text)
            else:
                r = requests.get(self.spilUrl + str(i), self.headers)
                self.spider(r.text)

if __name__ == '__main__':
    obj_spider = Qiushi()
    obj_spider.craw()
