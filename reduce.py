#!/usr/bin/python3
import sys
import collections
import happybase
host = "0.0.0.0"
table_name = "words1"
conn = happybase.Connection(host = host)
conn.open()
table = conn.table(table_name)
c ={}
for line in sys.stdin:#for each line in input
	line = line.strip()
	print(line)
	if(len(line.split(" ", 1))==2):
		count, word = line.split(" ", 1)# splits word based on tab spaces
		print("ad",count)
		print("aw",word)
		if count in c:
			c[count] += ","+(word)#increment by word frequency
		else:
			c[count]=word

dictn = sorted(c.items(), key= lambda a: a[1])
l = len(dictn)
for x in range(l):
	for val in dictn[x][1].split(","):
		table.put(dictn[x][0], {'counts:'+str(val): "0"})
conn.close()

