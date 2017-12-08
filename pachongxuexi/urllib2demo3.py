import urllib
import urllib2

#HTTP Get method

values = {}
values['username'] = "testname"
values['password'] = "testpwd"

data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data

request = urllib2.Request(geturl)
response = urllib2.urlopen(request)

print geturl
print response.read();
