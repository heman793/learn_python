import urllib2

#Handling Exceptions

request = urllib2.Request('http://www.xxx.com')
try:
	urllib2.urlopen(request)
except urllib2.URLError,e:
	print e.reason


