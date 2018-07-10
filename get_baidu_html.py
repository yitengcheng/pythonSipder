import requests

# r = requests.get('https://baidu.com')
# print(r.text)

# 模仿浏览器访问
# headers的意思就是告诉网站，我们是一个正常的浏览器在给它发送信息，请它给我们正确的信息。

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get('https://baidu.com', headers=headers)
print(r.text)
