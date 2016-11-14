'''
  pttstupidCrawer.py
  @about-craw 200 pages of jokes from ptt StupidClown 
  Created by 中皓 李 on 2016/10/24.
  Copyright © 2016 中皓 李. All rights reserved.
'''
import random
import json
from bs4 import BeautifulSoup #@note-(install via pip3)
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)

driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # enter PhantomJS executable_path 
pageOfJokes = 3187
jokeArray=[]
jokeArray.clear()
while (pageOfJokes != 2987):
	pageOfJokes = pageOfJokes - 1
	driver.get('https://www.ptt.cc/bbs/StupidClown/index'+str(pageOfJokes)+'.html') #find one page randomly
	pageSource = driver.page_source 
	soup = BeautifulSoup(pageSource, 'html.parser')
	articles =soup.findAll("div",{"class","r-ent"})
	for article in articles :
		jokeContent = {}
		jokeContent.clear()
		driver.get('https://www.ptt.cc'+article.a['href'])#find one article randomly
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
		if jokeContent:
			jokeArray.append(jokeContent)
if jokeArray:
	with open("joke.json", 'a') as out:
		out.write(json.dumps(jokeArray, out, ensure_ascii=False, indent=4))


	 


