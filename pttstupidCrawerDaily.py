'''
  pttstupidCrawerDaily.py
  @about-craw daily jokes from ptt StupidClown index page
  Created by 中皓 李 on 2016/11/10.
  Copyright © 2016 中皓 李. All rights reserved.
'''
import random
import datetime
from bs4 import BeautifulSoup #@note-(install via pip3)
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)
import time
import json

driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # enter PhantomJS executable_path 
driver.get('https://www.ptt.cc/bbs/StupidClown/index.html') #find one page randomly
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
now = datetime.datetime.now() #@note-get current time
articles =soup.findAll("div",{"class","r-ent"})
currentDate = time.strptime("{:02d}/{:02d}".format(now.month,now.day), "%m/%d") #@note-convert date string to datetime format for comparison
jokeArray=[]
jokeArray.clear()
for article in articles :
	articleDate = time.strptime(article.find("div",{"class","date"}).text.replace(' ', ''), "%m/%d")
	print(article.find("div",{"class","date"}).text.replace(' ', ''))
	if (currentDate == articleDate):
		jokeContent = {}
		jokeContent.clear()
		try:#prevent troubles from deleted articles
			articleURL=article.a['href']
		except:
 			continue
		driver.get('https://www.ptt.cc'+articleURL)#find one article randomly
		pageSource = driver.page_source 
		soup = BeautifulSoup(pageSource, 'html.parser')
		element =soup.findAll("div",{"class","bbs-screen bbs-content"},{"id","main-content"})	
		title= soup.findAll("span",{"class","article-meta-value"})
		if(soup.findAll("img")):
			continue
		try:#prevent troubles from deleted articles
			articleTitle=title[2].text
		except:
 			continue
		#sanitize unwanted contents 
		[s.extract() for s in soup('span')]
		[s.extract() for s in soup("div",{"class","push"})]
		[s.extract() for s in soup("div",{"class","richcontent"})]
		[s.extract() for s in soup("div",{"class","article-metaline"})]
		[s.extract() for s in soup("div",{"class","article-metaline-right"})]
		[s.extract() for s in soup('a')]
		#sanitize unwanted contents 
		jokeContent['title']= title[2].text
		jokeContent['date']= article.find("div",{"class","date"}).text
		jokeContent['context']=element[0].text.replace('"', '\"').replace("'", "\'")
		jokeArray.append(jokeContent)
if jokeArray :
	with open("{:02d}/{:02d}".format(now.month,now.day)+".json", 'a') as out:
		out.write(json.dumps(jokeArray))
		


	 

