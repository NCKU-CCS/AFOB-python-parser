'''
  ifoodieCrawer.py
  @about-Parse data from weekly ranking from ifoodie according to city 
  Created by 中皓 李 on 2016/10/18.
  Copyright © 2016 中皓 李. All rights reserved.
'''
import requests 
from bs4 import BeautifulSoup #@note-(install via pip3)
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)

city=''
requestURL = 'https://ifoodie.tw/ranking/weekly/'+city+'/' 
driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS
driver.get(requestURL)
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
result = soup.findAll("h4",{"class","title"})
for i in result: 
     print('https://ifoodie.tw'+i.a['href'])