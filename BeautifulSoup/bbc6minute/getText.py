#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url= "http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-170928"
r= requests.get(url)
parsed_html= BeautifulSoup(r.text, 'html.parser')
text= parsed_html.find_all("div", class_= "widget widget-richtext 6")
for x in text:
	print x