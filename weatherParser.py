'''
  weatherParser.py
  @about-Parse data from central weather bureau of taiwan according to the district of the target city and current time 
  Created by 中皓 李 on 2016/10/23.
  Copyright © 2016 中皓 李. All rights reserved.
'''
import json
import requests
import xmltodict #@note-convert xml to JSON format(install via pip3)
from bs4 import BeautifulSoup #@note-(install via pip3)
import dateutil.parser #@note-parse UTC time zone(install via pip3)

def getCityID(x):
    return {
        'yilan': 'F-D0047-001',
        'taoyuan': 'F-D0047-005',
        'hsinchuCounty': 'F-D0047-009',
        'miaoli': 'F-D0047-013',
        'changhua': 'F-D0047-017',
        'nantou': 'F-D0047-021',
        'yunlin': 'F-D0047-025',
        'chiayi': 'F-D0047-029',
        'Pingtung': 'F-D0047-033',
        'Taitung': 'F-D0047-037',
        'Hualien': 'F-D0047-041',
        'Penghu': 'F-D0047-045',
        'Keelung': 'F-D0047-049',
        'hsinchuCity': 'F-D0047-053',
        'chiayiCity': 'F-D0047-057',
        'taipei': 'F-D0047-061',
        'Kaohsiung': 'F-D0047-065',
        'newTaipeiCity': 'F-D0047-069',
        'Taichung': 'F-D0047-073',
        'tainan': 'F-D0047-077',
        'Lienchiang ': 'F-D0047-081',
        'Kinmen': 'F-D0047-085',
    }.get(x,9) 

currentTime=dateutil.parser.parse(str('')) #input current time 
city='' #input target city
district='' #input target district
developerAuthkey='CWB-335DC393-FCA8-4D15-9856-7AF060E0C210' #@note-Auth key need to be refreshed from time to time
cityId= getCityID(city) #input target city ID 
requestURL = 'http://opendata.cwb.gov.tw/opendataapi?dataid='+cityId+'&authorizationkey='+developerAuthkey

r = requests.get(requestURL)
paragraphs = """"""
if r.status_code == 200:
	soup = BeautifulSoup(r.text,"html.parser")
	s=soup.findAll("location")
	for letter in s:
		paragraphs+=str(letter)
	o = xmltodict.parse("<"+city+">"+paragraphs+"</"+city+">")
	for districtIndex, item in enumerate(o[city]['location']):
		if(o[city]['location'][districtIndex]['locationname']==district):
			break
	for timeIndex, item2 in enumerate(o[city]['location'][districtIndex]['weatherelement'][9]['time']): #@note-['weatherelement'][9] for full weather disciption
		if(dateutil.parser.parse(str(o[city]['location'][districtIndex]['weatherelement'][9]['time'][timeIndex]['starttime']))<=currentTime<=dateutil.parser.parse(str(o[city]['location'][districtIndex]['weatherelement'][9]['time'][timeIndex]['endtime']))):
			print(o[city]['location'][districtIndex]['weatherelement'][9]['time'][timeIndex]['elementvalue']['value'])
			break
		else:
			print('unable to find')
			break
else:
	r.raise_for_status()





