#!/usr/bin/python2

from stalkernet import stalkernet

net = stalkernet()
arr = net.buildArrayFromDict({"fname": ["and", "milo"]})
data = net.doRunQuery(arr)

for i in data:
  for k, v in i.iteritems():
    print k, v