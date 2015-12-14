import requests
from bs4 import BeautifulSoup as Soup

url = "http://www.immonet.de/angebot/26943825"
request = requests.get(url)
source = request.content

soup = Soup(source, 'lxml')

# price = soup.find("div", {'id': 'kfprice'})
# price = soup.find(id='kfprice')
price = soup.find('div', id='kfprice')

print price
# print price.prettify()
# print price.get_text()
# print price.span.string
#print price.span.get_text()
