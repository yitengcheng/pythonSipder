# encoding='utf-8'
from bs4 import BeautifulSoup
from html_down import Html_Down


class BaiduWenku(object):
    def __init__(self):
        self.html = Html_Down()
        self.file = open('./results/baiduTest.txt', 'a+')

    def spider(self, html):
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all('div')
            divs = soup.find_all('div', 'ie-fix')
            for div in divs:
                ps = div.find_all('p')
                for p in ps:
                    if p is None:
                        continue
                    else:
                        print(p.get_text())

    def craw(self, url):
        html = self.html.html(url)
        # print(html)
        self.spider(html)

if __name__ == '__main__':
    obj_spider = BaiduWenku()
    url = input('请输入网址')
    obj_spider.craw(url)
