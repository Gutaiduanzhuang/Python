import requests
import json
import time
import openpyxl

wb = openpyxl.Workbook()		# 实例化
ws = wb.active				# 激活 worksheet

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}			# 浏览器请求头

for id in range(1,101):			# 受到多方面因素的影响，这里仅演示对B站前200位用户进行爬取和分享

	str_id = str(id)			# 把int型数据string化
	
	response_1 = requests.get('https://api.bilibili.com/x/space/acc/info?mid=' + str_id + '&jsonp=jsonp', headers=headers)
	response_2 = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str_id + '&jsonp=jsonp', headers=headers)
	json_data_1 = json.loads(response_1.text)
	json_data_2 = json.loads(response_2.text)

	data_2 = json_data_2['data']			# 获取json文件2中的用户的data数据，其中包含用户id，关注用户数，粉丝数等等
	fans = data_2['follower']
	#time.sleep(0.3)				# 为了防止短时间内频繁访问服务器导致IP被封禁，这里用time库的sleep函数来延缓爬取速率

	if fans > 10000 :			# 查找粉丝数大于10000的B站用户，输出其昵称及粉丝数
		data_1 = json_data_1['data']		# 获取json文件1中的用户的data数据，其中包含用户昵称等
		name = data_1['name']				
		print('B站昵称：', name, '	', '粉丝数：', fans)			# 打印输出
		ws.append([name,fans])							# 存储数据



wb.save("F:\\公用的文件\\编程文件\\sublime的\\python\\爬虫\\B站百大up主粉丝数.xlsx")		# 保存数据到指定路径文件











# import requests
# import json

# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
# }

# for id in range(1,501):
# 	# url_1 = 'https://api.bilibili.com/x/web-interface/card?mid='
# 	str_id = str(id)
	
# 	response_1 = requests.get('https://api.bilibili.com/x/space/acc/info?mid=' + str_id + '&jsonp=jsonp', headers=headers)
# 	response_2 = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str_id + '&jsonp=jsonp', headers=headers)
# 	json_data_1 = json.loads(response_1.text)
# 	json_data_2 = json.loads(response_2.text)

# 	data_2 = json_data_2['data']
# 	# user_id = data_2['mid']
# 	fans = data_2['follower']
# 	# print(json_data_2)
# 	# print(data_2)
# 	if fans > 100000 :
# 		data_1 = json_data_1['data']
# 		name = data_1['name']
# 		print('B站昵称：', name, '	', '粉丝数：', fans)


# # # sel = page-follows > div > div.follow-sidenav > div.nav-container.topic-container > div.follow-list-container > ul > li > span.num


# # print(json_data)
