#!/usr/bin/env python3
## -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
baseUrl = 'https://www.qiushibaike.com'
spilUrl = 'https://www.qiushibaike.com/8hr/page/'
file = open('/Users/smt/Desktop/test.txt', 'a+')
for i in range(5):
    if i == 0:
        r = requests.get(baseUrl, headers)
        soup = BeautifulSoup(r.text, 'lxml')

        divs = soup.find_all('div', re.compile('^article'))
        for div in divs:
            if div.find_all('div','thumb'):
                continue
            elif div.find_all('div', 'content'):
                file.write(div.span.get_text())
                file.write('-----------------')
    else:
        r = requests.get(spilUrl + str(i), headers)
        soup = BeautifulSoup(r.text, 'lxml')

        divs = soup.find_all('div', re.compile('^article'))
        for div in divs:
            if div.find_all('div','thumb'):
                continue
            elif div.find_all('div', 'content'):
                file.write(div.span.get_text())
                file.write('-----------------\n' )
