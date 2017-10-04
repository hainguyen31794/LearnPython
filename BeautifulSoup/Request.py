import requests
from bs4 import BeautifulSoup
url = 'http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-170914'
r = requests.get(url)
parsed_html = BeautifulSoup(r.text, 'html.parser')
parsed_html.get_text().encode('utf-8')
target = open('titletech.html', 'w')
target.write(str((parsed_html.select("[class=text]"))[1]))
target.close()
