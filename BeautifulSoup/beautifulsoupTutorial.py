#-*- coding: utf-8 -*-
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link1">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup= BeautifulSoup(html_doc, 'html.parser')
# print soup.prettify() #format html_doc
# print soup.title #in title name
# print soup.title.name #in thẻ chứa title
# print soup.title.string #in title dạng chuỗi
# print soup.title.parent.name #in thẻ bố mẹ chứa title
# print type(soup.p)
# print len(soup.p['class'])
# print type(soup.a)
# #print soup.find_all("a" , id ="link1")
# print soup.find(id= "link1") # chỉ tìm được phần tử đầu tiên #type=<class 'bs4.element.Tag'>
for link in soup.find_all('a', id= "link1"):
	print link.get_text()# get('href')  = get link


