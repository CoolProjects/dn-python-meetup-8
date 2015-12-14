import requests
from bs4 import BeautifulSoup as Soup

url = "http://www.immonet.de/angebot/26943825"
request = requests.get(url)
source = request.content

soup = Soup(source, 'lxml')

price = soup.find(id='kfprice')
print price.span.string.strip()

room = soup.find(id='kfrooms')
print room.span.string.strip()
