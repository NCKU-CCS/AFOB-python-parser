'''
  pttstupidCrawer.py
  @about-craw random jokes from ptt StupidClown 
  Created by 中皓 李 on 2016/10/24.
  Copyright © 2016 中皓 李. All rights reserved.
'''
import requests
import random
from bs4 import BeautifulSoup #@note-(install via pip3)
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)

driver = webdriver.PhantomJS(executable_path=r'') # enter PhantomJS executable_path 
driver.get('https://www.ptt.cc/bbs/StupidClown/index'+str(random.randrange(1,3187))+'.html') #find one page randomly
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
topic=soup.findAll("div",{"class","title"})
driver.get('https://www.ptt.cc'+topic[random.randrange(1,20)].a['href'])#find one article randomly
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
article =soup.findAll("div",{"class","bbs-screen bbs-content"},{"id","main-content"})
#sanitize unwanted contents 
[s.extract() for s in soup('span')]
[s.extract() for s in soup("div",{"class","push"})]
[s.extract() for s in soup("div",{"class","richcontent"})]
[s.extract() for s in soup("div",{"class","article-metaline"})]
[s.extract() for s in soup("div",{"class","article-metaline-right"})]
[s.extract() for s in soup('a')]
#sanitize unwanted contents 
print(article[0].text)
