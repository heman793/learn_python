#!/usr/bin/python
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
print 'jsonData type:',type(jsonData)
print 'jsonData:\n',jsonData

text = json.loads(jsonData)
print 'text type:',type(text)
print 'text:\n',text
