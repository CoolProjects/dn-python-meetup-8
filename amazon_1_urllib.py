import urllib2


f = urllib2.urlopen("http://www.amazon.co.uk/")
print f.read()
