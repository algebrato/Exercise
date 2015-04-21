#!/usr/bin/python

import MySQLdb
import getpass

try:
	#server = raw_input('Server: ')
	server = "92.222.24.64"
	#uid = raw_input('User: ')
	uid ="root"
	pwd = getpass.getpass()
except:
	print("ERRORRRRRR!!!!!!")

try:
	db = MySQLdb.connect(host=server, user=uid, passwd=pwd, db="Syslog")
except:
	print ""
	print("Error connection database...")
	quit()

try:
	print ""
	print "Fetching ..."
	print ""
	cur = db.cursor();
	cur.execute("select * from SystemEvents")
	for row in cur.fetchall() :
		print row[3],row[20],row[7]
except:
	print ""
	print("Errore passo 2")
