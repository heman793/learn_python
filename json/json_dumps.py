#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
print 'data type:',type(data)
print 'data:\n',data

json = json.dumps(data)
print 'json type:',type(json)
print 'json:\n',json
