# 爬取京东鞋子/口红数据，保存到excel数据表，并可视化

import requests
import json
import openpyxl

wk = openpyxl.Workbook()
sheet = wk.create_sheet()

# resp = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8138773&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
resp = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100001999907&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
content = resp.text

rest = content.replace('fetchJSON_comment98(','').replace(');','')

json_data = json.loads(rest)
comments = json_data['comments']

for item in comments:
	color = item['productColor']
	size = item['productSize']
	# print(color)
	# print(size)
	sheet.append([color,size])
	wk.save('F:\\公用的文件\\编程文件\\sublime的\\python\\爬虫\\京东销售数据1.xlsx')


