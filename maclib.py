#!/usr/bin/python3
import subprocess
import re
import json
import requests
from decimal import (Decimal, ROUND_DOWN)
#import apim
#import sqlite3
import urllib
import MySQLdb
import configparser
import math
import mlibs
import uuid
config = configparser.ConfigParser()
config.read('dismona.conf')

section1 = 'complylaw'
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')

connection = MySQLdb.connect(
	host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
cursor = connection.cursor()

def getusersaddress(userid):
	print("GETUSERSADDRESS")
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	cursor.execute("SELECT address FROM accounts WHERE discordid='{}'".format(userid))
	#print(cursor.fetchone())
	print("userid:" + userid)
	address = cursor.fetchall()
	print(address)
	#address = fixselect(address)
	addressl = list(address)
	print(addressl)
	try:
		address = addressl[0]
		print(address)
		print("TYPEADDRESS", type(address))
		address = address[0]
		return address
	except:
		return "NF"

def reguseraddress(discordid, regaddress):
	#prevuseradd = getusersaddress(discordid)
	#remuseraddress(discordid)
	if mlibs.validateaddress(regaddress):
		res = getusersaddress(discordid)
		if res == "NF" or res == "null" or res == "None":
			connection = MySQLdb.connect(
				host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
			cursor = connection.cursor()
			cursor.execute("INSERT INTO accounts (discordid, address) VALUES (%s, %s)", (discordid, regaddress,))
			connection.commit()
			print("INSERTING TO DATABASE SUCCEEDED.")
			updatemonageid(discordid)
			return True
		else:
			print("Wasn't NF")
			return False
	else:
		return False

def updateuseraddress(discordid, newaddress):
	if mlibs.validateaddress(newaddress):
		if getusersaddress(discordid) != "NF":
			connection = MySQLdb.connect(
				host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
			cursor = connection.cursor()
			cursor.execute("UPDATE accounts SET address = '{0}' WHERE discordid = '{1}'".format(newaddress, discordid))
			connection.commit()
			print("INSERTING TO DATABASE SUCCEEDED.")
			return True
		else:
			print("Was NF")
			return False
	else:
		return False

def getmonageid(discordid):
	if getusersaddress(discordid) != "NF":
		print("Wasn't NF")
		cursor.execute("SELECT monageid FROM accounts WHERE discordid='{}'".format(discordid))
		print("SELECT monageid FROM accounts WHERE discordid='{}'".format(discordid))
		monageid = cursor.fetchall()
		print(monageid)
		monageid = str(monageid[0])
		monageid = str(mlibs.fixselect(monageid))
		return monageid
	else:
		return "ERROR"

def generatemonageid():
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	useruuid = str(uuid.uuid4())
	useruuid = useruuid.replace("-", "") #ハイフン削除
	#TODO:UUIDが衝突しないか一応チェック入れること
	cursor.execute("SELECT monageid FROM accounts")
	res = cursor.fetchall()
	connection.close()
	if useruuid in str(res):
		return "REDO"
	else:
		return useruuid

def createmonageid(discordid):
	monageid = generatemonageid()
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	if "REDO" not in monageid:
		print("INSERT INTO accounts (monageid, discordid) VALUES ('{0}', '{1}')".format(monageid, discordid))
		cursor.execute("INSERT INTO accounts (monageid, discordid) VALUES ('{0}', '{1}')".format(monageid, discordid))
		connection.commit()
		return True
	else:
		return False

def updatemonageid(discordid):
	monageid = generatemonageid()
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	if "REDO" not in monageid:
		cursor.execute("UPDATE accounts SET monageid = '{0}' WHERE discordid = '{1}'".format(monageid, discordid))
		connection.commit()
