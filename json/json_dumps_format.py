#!/usr/bin/python
import json


data = {'a':'Runoob','b':7}
print 'data type:',type(data)
print 'data:\n',data

json = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'))
print 'json type:',type(json)
print 'json:\n',json



