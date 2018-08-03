# enconding='utf-8'
from selenium import webdriver
import time


class Html(object):
	def __init__(self):
		self.browser = webdriver.Chrome()

	def sipder(self,url):
		self.browser.get(url)
	    #找到继续阅读按钮的上一级div,banner-more-btn是div的类名用.,ID用#
		hidden_div = self.browser.find_element_by_css_selector("#html-reader-go-more")
	    #获取阅读按钮
		gotBtn = self.browser.find_element_by_css_selector("#html-reader-go-more .banner-more-btn")
		actions = webdriver.ActionChains(self.browser)
		actions.move_to_element(hidden_div)
		actions.click(gotBtn)
		actions.perform()
		
		#获取文章标题
		title = self.browser.find_element_by_xpath("//*[@id=\"doc-tittle-0\"]").text
		file = open('C:/Users/Administrator/Desktop/' + title + '.txt', 'a+', encoding='utf-8')

		time.sleep(3)
	    #获取包含内容的div 
		div_text = self.browser.find_elements_by_class_name("ie-fix")
		for temp in div_text:
			text = temp.text
			file.write(text)


if __name__ == "__main__":
	html = Html()
	src = input('请输入网址')
	html.sipder(src)
    
