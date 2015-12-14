import requests

request = requests.get("http://www.amazon.co.uk/")
source = request.content

print source
