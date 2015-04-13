#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="xxxx", user="root", passwd="xxxxx", db="mysql")
cur = db.cursor();
cur.execute("select * from user")
for row in cur.fetchall() :
	print row[0] + "\t" + row[1]

db.close()
