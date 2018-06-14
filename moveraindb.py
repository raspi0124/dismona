import sqlite3
import MySQLdb

mconnection = MySQLdb.connect(
   host='localhost', user='root', passwd='laksjd', db='dismona', charset='utf8')
mcursor = mconnection.cursor()
mcursor.execute("CREATE TABLE IF NOT EXISTS rainregistered (rainid VARCHAR(50));")
dbpath = 'dismona.sqlite'
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
cursor.execute('SELECT * FROM rainregistered ORDER BY rainid')
rainall = cursor.fetchall()
rainall = str(rainall)
pattern=r'([+]?[0-9]+\.?[0-9]*)'
rainall = re.findall(pattern,rainall)
print(rainall)
