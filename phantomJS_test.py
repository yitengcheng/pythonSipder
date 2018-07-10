# encoding='utf-8'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://wenku.baidu.com/view/bb250f2bbd64783e09122b8c.html?sxts=15\
	31242255906')
data = driver.page_source
soup = BeautifulSoup(data, 'lxml')
divs = soup.find_all('div', 'ie-fix')
for div in divs:
	ps = div.find_all('p')
	for p in ps:
		print(p.get_text())

	# if div.p is None:
	# 	continue
	# else:
	# 	print(div.p.get_text())
