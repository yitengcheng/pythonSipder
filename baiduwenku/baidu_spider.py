# enconding='utf-8'
from selenium import webdriver
import time


if __name__ == "__main__":
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
	browser = webdriver.Chrome(chrome_options=options)
	browser.get("https://wenku.baidu.com/search?word= &lm=0&od=0&fr=top_home&ie=gbk")
	# 通过ID找网页标签,找到搜索框标签
	seek_input = browser.find_element_by_id('kw')
	# 设置搜索内容
	content = "饮料"
	seek_input.send_keys(content)

	# 找到搜索文档按钮
	seek_but = browser.find_element_by_id('sb')
	# 并且点击搜索按钮
	seek_but.click()
	while True:
		#获取所有的文档a标签,这里的elements指的是有多个元素,*表示的是任意的(xpath中可以使用)
		all_a = browser.find_elements_by_xpath("//*[@id=\"bd\"]/div[1]/div[1]/div[5]/div[1]/dl[*]/dt[1]/p[1]/a[1]")
		for a in all_a:
			#attribute对象表示Html的属性
			print(a.get_attribute("href"))
			print(a.get_attribute("title"))
		#获取body中html标签
		body = browser.find_element_by_tag_name("body")
		body_html = body.get_attribute("innerHTML")
		#判断下一页按钮是否存在
		flag = str(body_html).find("class=\"next\"")
		if flag != -1:
			#获取下一页按钮的标签,这里用class标签,因为它只有一个
			next_page = browser.find_element_by_class_name("next")
			#点击下一页按钮
			next_page.click()
			#点击之后,睡眠5s,防止页面没有加载完全,报no such element的错误
			time.sleep(5)
		else :
			break