'''
  ifoodieCrawer.py
  @about-Parse data from weekly ranking from ifoodie according to city 
  Created by 中皓 李 on 2016/10/18.
  Copyright © 2016 中皓 李. All rights reserved.
'''
from urllib.parse import quote 
import random
from bs4 import BeautifulSoup #@note-(install via pip3)
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)
import json

meals=['早餐','午餐','晚餐']
cities={
	'台北':['中正區','大同區','中山區','松山區','大安區','萬華區','信義區','士林區','北投區','內湖區','南港區','文山區','萬里','金山','板橋','汐止','深坑','石碇','瑞芳','平溪','雙溪','貢寮','新店','坪林','烏來','永和','中和','土城','三峽','樹林','鶯歌','三重','新莊','泰山','林口','蘆洲','五股','八里','淡水','三芝','石門'],
	'高雄':['新興區','前金區','苓雅區','鹽埕區','鼓山區','旗津區','前鎮區','三民區','楠梓區','小港區','左營區','仁武','大社','岡山','路竹','阿蓮','田寮','燕巢','橋頭','梓官','彌陀','永安','湖內','鳳山','大寮','林園','鳥松','大樹','旗山','美濃','六龜','內門','杉林','甲仙','桃源','三民','茂林','茄萣'],
	'台南':['中區','東區','南區','西區','北區','安平區','安南區','永康','歸仁','新化','左鎮','玉井','楠西','南化','仁德','關廟','龍崎','官田','麻豆','佳里','西港','七股','將軍','學甲','北門','新營','後壁','東山','六甲','下營','柳營','鹽水','善化','大內','山上','新市','安定'],
	'台中':['中區','東區','南區','西區','北區','北屯區','西屯區','南屯區','太平','大里','霧峰','烏日','豐原','后里','石岡','東勢','和平','新社','潭子','大雅','神岡','大肚','沙鹿','龍井','梧棲','清水','大甲','外埔','大安'],
    '桃園':['中壢','平鎮','龍潭','楊梅','新屋','觀音','桃園','龜山','八德','大溪','復興','大園','蘆竹'],
	'宜蘭':['宜蘭','頭城','礁溪','壯圍','員山','羅東','三星','大同','五結','冬山','蘇澳','南澳'],
	'新竹':['北區','東區','香山區','竹北','湖口','新豐','新埔','關西','芎林','寶山','竹東','西湖','五峰','橫山','尖石','北埔','峨眉'],
	'嘉義':['番路','梅山','竹崎','阿里山','中埔','大埔','水上','路草','太保','朴子','東石','六腳','新港','民雄','大林','溪口','義竹','布袋'],
	'彰化':['彰化','芬園','花壇','秀水','鹿港','福興','線西','和美','伸港','員林','社頭','永靖','埔心','溪湖','大村','埔鹽','田中','北斗','田尾','埤頭','溪洲','竹堂','二林','大城','芳苑','二水'],
	'基隆':['仁愛區','信義區','中正區','中山區','安樂區','暖暖區','七堵'],
	'花蓮':['花蓮市','新城','秀林','吉安','壽豐','鳳林','光復','豐濱','瑞穗','萬榮','玉里','卓溪','富里'],
	'南投':['南投市','中寮','草屯','國姓','埔里','仁愛','名間','集集','水里','魚池','信義','竹山','鹿谷'],
	'苗栗':['竹南','頭份','三灣','南庄','獅潭','後龍','通宵','苑裡','苗栗','造橋','頭屋','公館','大湖','泰安','銅鑼','三義','西湖','卓蘭'],
	'屏東':['屏東市','三地','霧臺','瑪家','九如','里港','高樹','鹽埔','長治','麟洛','竹田','內埔','萬丹','潮州','泰武','來義','萬巒','崁頂','新埤','南州','林邊','東港','琉球','佳冬','新園','枋寮','枋山','春日','獅子','車城','牡丹','恆春','滿州'],
	'雲林':['斗南','大埤','虎尾','土庫','褒忠','東勢','臺西','崙背','麥寮','斗六','林內','古坑','荊桐','西螺','二崙','北港','水林','口湖','四湖','元長'],
	'台東':['台東市','鹿野','成功','達仁']
}

driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS

def brewSoup(requestURL):
	driver.get(requestURL)
	pageSource = driver.page_source 
	return BeautifulSoup(pageSource, 'html.parser')



for city in list(cities.keys()):
	city='台南'#@note-debug mode
	print(city)#@note-debug mode
	for district in cities[city] :
		district='東區'#@note-debug mode
		print(district)#@note-debug mode
		restaurantInfo = []
		restaurantInfo.clear()
		for mealtype in meals :
			print('query='+city+'+'+district+'+'+mealtype)#@note-debug mode
			requestURL= 'https://ifoodie.tw/city/'+quote(city)+'?q='+quote(district)+quote(' ')+quote(mealtype)
			soup = brewSoup(requestURL)
			result = soup.findAll("div",{"class","title media-heading"}) 
			if not result :
				break
			print(mealtype)
			for store in result:
				storeContent = {}
				storeContent.clear()
				storeContent['category']={}
				storeContent['category'].clear()
				if storeContent['category']:
					storeContent['category'].extend([mealtype])
				else:
					storeContent['category']=[mealtype]
				storeRequestUrl='https://ifoodie.tw'+store.a['href'];
				soup=brewSoup(storeRequestUrl)
				restaurantName=soup.findAll("div",{"class","restaurant item right"})
				if not restaurantName[0].h4.a.text:
					continue
				breakFlag = False
				for item in restaurantInfo :
					if(breakFlag):
						print('break outerloop')
						break
					if item :
						if(item['name']==restaurantName[0].h4.a.text) :
							for aaa in item['category']:
								if(aaa==mealtype):
									breakFlag = True
									break
							if not breakFlag :
								item['category'].extend([mealtype])
								breakFlag=True
					if(breakFlag):
						break
				if(breakFlag):
					continue
				storeContent['name']=restaurantName[0].h4.a.text
				restaurantAddr = soup.findAll("div",{"class","address right"})
				storeContent['address']=restaurantAddr[0].text
				storeContent['link']=storeRequestUrl
				restaurantInfo.append(storeContent)
		if restaurantInfo :
			with open(city+"-"+district+".json", 'a') as out:
				out.write(json.dumps(restaurantInfo, ensure_ascii=False, indent=4))
		break #@note-break_distric-debug mode
	break #@note-break-city-debug mode