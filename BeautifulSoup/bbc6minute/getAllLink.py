import requests
from bs4 import BeautifulSoup
url= "http://www.bbc.co.uk/learningenglish/english/features/6-minute-english"
r= requests.get(url)
parsed_html= BeautifulSoup(r.text, 'html.parser')
# print parsed_html.get_text().encode('utf-8')
kq= parsed_html.find_all('a')
target= []
for x in kq:
	if str(x.get('href')).find("features/6-minute-english/ep")!= -1:
		target.append('http://www.bbc.co.uk'+str(x.get('href')))
# -----------------------------------------------------------------------#




