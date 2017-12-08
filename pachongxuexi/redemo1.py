import re

pattern = re.compile(r'hello')

result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloooooo world')
result3 = re.match(pattern,'helo world')
result4 = re.match(pattern,'hello world')

if result1:
	print result1.group()
else:
	print '1 match fail'

if result2:
	print result2.group()
else:
	print '2 match fail'

if result3:
	print result3.group()
else:
	print '3 match fail'

if result4:
	print result4.group()
else:
	print  '4 match fail'










