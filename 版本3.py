from bs4 import BeautifulSoup
import requests
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# 上面的三对双引号表示多行字符串，也可用于表示多行注释

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

response = requests.get('https://space.bilibili.com/2/fans/fans', headers=headers)
response.encoding = 'utf-8'

# print(response.text)

# soup = BeautifulSoup(response.text,features='lxml')
soup = BeautifulSoup(response.text,'html.parser')

print(soup.prettify)