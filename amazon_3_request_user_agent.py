import requests

# headers = {
#     'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
#                   ' AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/47.0.2526.73 Safari/537.36'}

# request = requests.get('http://demosite.jaljale.com/test.php', headers=headers)
request = requests.get('http://demosite.jaljale.com/test.php')
source = request.content

print source
