import urllib2

url = "https://translate.google.com/translate_a/single?client=t&sl=en&hl=en&dt=t&ie=UTF-8&oe=UTF-8&otf=1&rom=1&ssel=0&tsel=0&kc=2&tk=21140.423657&q="
i = 0
phrase = "i love you"

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
    print "%s. %s: %s" % (i, val, translate_url)

    f = urllib2.urlopen(translate_url)
    print f.read()

    break