#!/usr/bin/python3
import sys
import collections
import happybase
from collections import OrderedDict
host = "0.0.0.0"
table_name = "words"
conn = happybase.Connection(host = host)
conn.open()
dictn={}
table = conn.table(table_name)
while True:
    for key,data in table.scan():
      key1=str(key).replace("b'","").replace("b\"","")[:-1]
      data1=str(data).replace("{b'counts:wordcount': b'","")[:-2]
      print(data1,key1)
    break
conn.close()

