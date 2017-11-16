
from bs4 import BeautifulSoup
import lxml
import requests

url='http://www.facebook.com'

html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc,'lxml')

tags = soup('a')
for tag in tags:
  print(tag.get('href',None))
