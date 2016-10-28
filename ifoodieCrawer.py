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

city='台南'
district='北區'
meal='早餐'
requestURL= 'https://ifoodie.tw/city/'+quote(city)+'?q='+quote(district)+quote(' ')+quote(meal)
driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS
driver.get(requestURL)
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
result = soup.findAll("div",{"class","title media-heading"}) 
storeRequestUrl='https://ifoodie.tw'+result[random.randrange(1,len(result))].a['href'];
driver.get(storeRequestUrl)
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
restaurantName = soup.findAll("div",{"class","restaurant item right"})
print(restaurantName[0].h4.a.text)
restaurantAddr = soup.findAll("div",{"class","address right"})
print(restaurantAddr[0].text)
print(storeRequestUrl)