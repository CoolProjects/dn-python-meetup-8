import mechanize

br = mechanize.Browser()

br.addheaders = [('User-agent',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/47.0.2526.73 Safari/537.36')]
r1 = br.open("http://www.amazon.co.uk/")

br.follow_link(url_regex='sign-in-redirect')
print(br.read())
