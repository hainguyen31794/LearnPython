import requests
from bs4 import BeautifulSoup
url= "http://dict.laban.vn/find?type=1&query=hallo"
r= requests.get(url)
parsed_html= BeautifulSoup(r.text, 'html.parser')
print type(parsed_html.title) #<class 'bs4.element.Tag'>
print parsed_html.title.string
soup
#print parsed_html.get_text().encode('utf-8')