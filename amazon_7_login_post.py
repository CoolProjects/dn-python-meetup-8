import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [(
    'User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
    ' AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/47.0.2526.73 Safari/537.36')]
r1 = br.open("http://www.amazon.co.uk/")

br.follow_link(url_regex='sign-in-redirect')

br.select_form(name="signIn")
br['email'] = '--------your email address--------'
br['password'] = '--------password--------'
res = br.submit()

print(res.read())
