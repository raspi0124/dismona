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
from maclib import *
import maclib
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

def round_down5(value):
	value = Decimal(value).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)
	return str(value)
def getcurrentprice():
	headers = {
	'Accept': 'application/json',
	}
	response = requests.get('https://public.bitbank.cc/mona_jpy/ticker', headers=headers)
	response = response.json()
	data = response['data']
	currentprice = data['last']
	currentprice = str(currentprice)
	return currentprice
def helloworld():
	return "Hello World"

def libgetjpybalance(userid):
	headers = {
	'Accept': 'application/json',
	}
	response = requests.get('https://public.bitbank.cc/mona_jpy/ticker', headers=headers)
	response = response.json()
	data = response['data']
	currentprice = data['last']
	currentprice = str(currentprice)
	currentprice = float(currentprice)

	balance = libgetbalance(maclib.getusersaddress(userid))
	balance = float(balance)
	jpybalance = float(currentprice) * float(balance)
	balance = str(balance)
	jpybalance = str(jpybalance)
	return jpybalance

def libgetbalance(address):
	#Getbalance in new version, requesting blockbook a balance.
	address = str(address)
	headers = {
	'Accept': 'application/json',
	}
	requestto = 'https://blockbook.electrum-mona.org/api/v2/address/' + address + '?details=basic'
	print(requestto)
	response = requests.get(requestto, headers=headers)
	print(response)
	response = response.json()
	print(response)
	balance = int(response['balance'])
	addresstomakesure = str(response['address'])
	watanabevalue = float(100000000)
	balance = balance / watanabevalue
	balance = float(balance)
	if addresstomakesure == address:
		return balance
	else:
		return "GNB_E" #When responsed address does not match with requested address. Probably won't happen.


def deposit(userid):
	return maclib.getusersaddress(userid)

def getunconfbalance(userid):
	#Getbalance in new version, requesting blockbook a balance.
	address = str(maclib.getusersaddress(userid))
	headers = {
	'Accept': 'application/json',
	}
	response = requests.get('https://blockbook.electrum-mona.org/api/v2/address/' + address + '?details=basic', headers=headers)
	response = response.json()
	balance = str(response['balance'])
	addresstomakesure = str(response['address'])
	return balancelib

def withdraw(userid, to, amount):
	return "CMDNOLONGERWORKS"


def tip(userid, to, amount):
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	balance = libgetbalance(maclib.getusersaddress(userid))
	toaddress = maclib.getusersaddress(to)
	#cursor.execute("INSERT INTO tipqueue (id, to, amount) VALUES (%s, %s, %s)", (userid, to, amount))
	#json = {
	#	"type": "tip",
	#	"to": "toaddress",
	#	"from": "fromaddress",
	#	"id": "00000000"
	#}
	#TODO:ってか下のやつゆくゆくはtoをMonage IDにしてクライアント側でアドレス照合したいなー
	return "https://mpursetest2.raspi0124.dev/send.html?sendto=" + toaddress + "&amount=" + amount + "&memo=from_" + userid

def fixselect(string):
	string = str(string)
	string = string.replace('(', '')
	string = string.replace(')', '')
	string = string.replace("b'", '')
	string = string.replace("'", '')
	string = string.replace(",,", ',')
	string = string.replace("[", '')
	string = string.replace("]", '')
	string = string.replace("['", "")
	string = string.replace("'", "")
	string = string.replace("', '']", "")
	#string = string.split(',')
	string = str(string)
	return string


def getpubkey(address):
	cmd = "monacoin-cli validateaddress {}".format(address)
	print(cmd)
	rut  =  subprocess.check_output( cmd.split(" ") )
	rut = rut.decode()
	rut = str(rut)
	rut = rut.replace("\n", '')
	resultjson = rut
	print(resultjson)
	resultjson = json.loads(resultjson)
	print(json.dumps(resultjson["pubkey"]))
	pubkey = json.dumps(resultjson["pubkey"])
	print(pubkey)
	return pubkey

def isurlexist(url):
	if re.match(r"^https?:\/\/", url):
		try:
			res = urllib.request.urlopen(url)
			res.close()
			return "1" #Success
		except urllib.error.HTTPError as e:
			print(e)
			return "0-1" #HTTPError
		except urllib.error.URLError as e:
			print(e)
			return "0-2" #Notfound
	else:
		return "0" #Not URL

def sqlformat_faucet(msg):
	msg = str(msg)
	msg = msg.replace('(', '')
	msg = msg.replace(')', '')
	msg = msg.replace("b'", '')
	msg = msg.replace("'", '')
	msg = msg.replace(",,", ',')
	msg = msg.replace("[", '')
	msg = msg.replace("]", '')
	msg = msg.split(',')
	msg = str(msg)

def validateaddress(address):
	cmd = "monacoin-cli validateaddress {}".format(address)
	print(cmd)
	rut  =  subprocess.check_output( cmd.split(" ") )
	print(rut)
	rut = rut.decode()
	rut = str(rut)
	rut = rut.replace("\n", "")
	resultjson = rut
	print(resultjson)
	resultjson = json.loads(resultjson)
	print(resultjson)
	isvalid = resultjson["isvalid"]
	print(isvalid)
	if "True" in str(isvalid):
		return True
	else:
		return False
