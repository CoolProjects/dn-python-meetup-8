import mechanize

br = mechanize.Browser()

r1 = br.open("http://www.amazon.co.uk/")

br.follow_link(url_regex='sign-in-redirect')
print(br.read())
