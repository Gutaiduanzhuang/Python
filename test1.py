# 谁是今年的百大up主？爬虫告诉你！
import requests
import json
import time

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}			# 浏览器请求头，让python的网络请求更加逼真——模仿浏览器的请求，可以在Google浏览器中输入about:version查看自己的，对B站而言，可加可不加

for id in range(1,201):			# 受到多方面因素的影响，这里仅演示对B站前200位用户进行爬取和分享，你可以自己改变范围

	str_id = str(id)			# 把int型数据string化
	
	response_1 = requests.get('https://api.bilibili.com/x/space/acc/info?mid=' + str_id + '&jsonp=jsonp', headers=headers)
	response_2 = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str_id + '&jsonp=jsonp', headers=headers)
	json_data_1 = json.loads(response_1.text)
	json_data_2 = json.loads(response_2.text)

	data_2 = json_data_2['data']			# 获取json文件2中的用户的data数据，其中包含用户id，关注用户数，粉丝数等等
	fans = data_2['follower']
	time.sleep(1)				# 为了防止短时间内频繁访问服务器导致IP被封禁，这里用time库的sleep函数来延缓爬取速率，但是爬取速率会大打折扣，但如果你追求速度，觉得暂时几个小时不看B站也没什么问题的话，可以去掉这一行

	if fans > 100000 :			# 查找粉丝数大于10万（这个你也可以自己改，改成100万输出的差不多就是百大up主了吧）的B站用户，输出其昵称及粉丝数
		data_1 = json_data_1['data']		# 获取json文件1中的用户的data数据，其中包含用户昵称等
		name = data_1['name']				
		print('B站昵称：', name, '	', '粉丝数：', fans)		