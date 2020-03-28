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
from mlibs import *
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
	address = addressl[-1]
	print(address)
	address = address[-1]
	return address

def reguseraddress(userid, regaddress):
	#prevuseradd = getusersaddress(userid)
	#remuseraddress(userid)
	if validateaddress(regaddress):
		connection = MySQLdb.connect(
			host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
		cursor = connection.cursor()
		cursor.execute("INSERT INTO accounts (discordid, address) VALUES (%s, %s)", (userid, regaddress,))
		connection.commit()
		connection.close()
		return True
	else:
		return False

def getmonageid(discordid):
	cursor.execute("SELECT discordid FROM accounts")
	accountDB = cursor.fetchall()
	if discordid in accountDB:
		cursor.execute("SELECT monageid FROM accounts WHERE discordid='{}'".format(discordid))
		monageid = cursor.fetchall()
		monageid = str(monageid)
		return monageid
	else:
		return "ERROR"

def generatemonageid():
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	uuid = str(uuid.uuid4())
	#TODO:UUIDが衝突しないか一応チェック入れること
	cursor.execute("SELECT monageid FROM accounts")
	res = cursor.fetchall()
	connection.close()
	if uuid in str(res):
		return "REDO"
	else:
		return uuid

def createmonageid(discordid):
	monageid = generatemonageid()
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	if "REDO" not in monageid:
		cursor.execute("INSERT INTO accounts (monageid) VALUES ('{0}') WHERE discordid='{1}'".format(monageid, userid))
		connection.commit()
