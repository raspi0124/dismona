import sqlite3
import MySQLdb
import re

mconnection = MySQLdb.connect(
   host='localhost', user='root', passwd='laksjd', db='dismona', charset='utf8')
mcursor = mconnection.cursor()
dbpath = '/root/dismona.sqlite'
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
cursor.execute('SELECT * FROM rainregistered ORDER BY rainid')
rainall = cursor.fetchall()
rainall = str(rainall)
pattern=r'([+]?[0-9]+\.?[0-9]*)'
rainall = re.findall(pattern,rainall)
print(rainall)

for x in rainall:
	mcursor.execute("INSERT INTO rainregistered(rainid) VALUES (%s)", (x,))
	print(x)
mconnection.commit()
mconnection.close()
