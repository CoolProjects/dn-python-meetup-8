import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')]


url = "https://translate.google.com/translate_a/single?client=t&sl=en&hl=en" \
      "&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&"  \
      "oe=UTF-8&otf=1&rom=1&ssel=0&tsel=0&kc=2&tk=21140.423657&q="

i = 0
phrase = "i%20love%20you"

to = {
    'es': 'Spanish',
    'ne': 'Nepali',
    'hi': 'Hindi',
    'nl': 'Dutch',
    'fi': 'Finish',
    'fr': 'French',
    'iw': 'Hibrew',
    'ja': 'Japanese',
    'zh-CN': 'Chinese Simplified',
    'ko': 'Korean'}

print "Translation of %s into %s langauges'" % (phrase, len(to))

for key, val in to.iteritems():
    translate_url = '%s%s&tl=%s' % (url, phrase, key)
    i += 1
    print "%s. %s" % (i, val)

    res = br.open(translate_url)
    print res.read()
    print ""
