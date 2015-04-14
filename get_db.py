#!/usr/bin/python

import MySQLdb
import getpass

try:
	server = raw_input('Server: ')
	uid = raw_input('User: ')
	pwd = getpass.getpass()
except:
	print("ERRORRRRRR!!!!!!")

try:
	db = MySQLdb.connect(host=server, user=uid, passwd=pwd, db="mysql")
except:
	print ""
	print("Error connection database...")
	quit()

try:
	print ""
	print "Fetching ..."
	print ""
	cur = db.cursor();
	cur.execute("select * from user")
	for row in cur.fetchall() :
		print row[0] + "\t" + row[1]
	db.close()
except:
	print ""
	print("Errore passo 2")
