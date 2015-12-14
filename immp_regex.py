import requests
import re
from bs4 import BeautifulSoup as Soup

url = "http://www.immonet.de/angebot/26943825"
request = requests.get(url)
source = request.content

print source

soup = Soup(source, 'lxml')

price = soup.find(id='kfprice')
price = price.span.string.strip()
price = re.search('(\d+.\d+)', price).group()[0]

room = soup.find(id='kfrooms')
room = room.span.string.strip()

js_pattern = re.compile('dataLayer\.push\(\{(.*?)\}\);')
js_part = js_pattern.findall(source)

try:
    js_part = js_part[0]
except:
    js_pattern = ''

try:
    zip = re.compile('"zip":"(.*?)"').findall(js_part)[0]
except:
    zip = ''

print "Price: %s, Room: %s, Zip: %s" % (price, room, zip)
