# encoding='utf-8'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Html_Down(object):
	def html(self, url):
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get(url)
		html = driver.page_source
		return html
