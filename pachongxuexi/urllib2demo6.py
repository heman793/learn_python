import urllib2

request = urllib2.Request('http://blog.csdn.net/abc')
try:
	urllib2.urlopen(request)
except urllib2.HTTPError,e:
	print e.code
	print e.reason

