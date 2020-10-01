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

def getoldbalance(userid):
	unlockwallet()
	minconf = "60"
	cmdlib = "monacoin-cli getbalance {0} {1}".format(userid, minconf)
	rutlib = subprocess.check_output( cmdlib.split(" ") )
	balancelib = rutlib.decode()
	balancelib = float(balancelib)
	balancelib = str(balancelib)
	return balancelib
	
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

def withdraw_old(userid, to, amount):
	unlockwallet()
	balancea = libgetbalance(userid)
	fee = "0.000001"
	reamount = float(amount) - float(fee)
	reamount = round_down5(reamount)
	reamount = str(reamount)
	minbalance = "0.00001"
	minbalance = float(minbalance)
	minamount = "0.00001"
	minamount = float(minamount)
	balancea = float(balancea)
	amount = float(amount)
	if amount >= minamount:
		if amount <= balancea:
			cmd = "monacoin-cli sendfrom {0} {1} {2}".format(userid, to, reamount)
			rut  =  subprocess.check_output( cmd.split(" ") )
			cmd = "monacoin-cli move {0} fee {1}".format(userid, fee)
			subprocess.check_output( cmd.split(" ") )
			rut = rut.decode()
			m = rut
			balancea = libgetbalance(userid)
			if balancea <= "0":
				defo = "0"
				amounttosendback = float(defo) - float(balancea)
				amounttosendback = str(amounttosendback)
				cmd = "monacoin-cli move fee {0} {1}".format(userid, amounttosendback)
				subprocess.check_output( cmd.split(" ") )

		else:
			#m = "<@" + userid + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"
			m = "500"
	else:
		#m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
		m = "500"
	return m

def tip(userid, to, amount):
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	balance = libgetbalance(maclib.getusersaddress(userid))
	frommonageid = maclib.getmonageid(userid)
	toaddress = maclib.getusersaddress(to)
	print("TIPDEBUG", toaddress)
	if toaddress != "NF":
		return "https://mpursetest2.raspi0124.dev/send.html?sendto=" + toaddress + "&amount=" + amount + "&memo=from_" + frommonageid
	else:
		return "Tip先のユーザーは現在アドレスが登録されていないようです。/checkaddress @ユーザー名 でそのユーザーがアドレスを登録されているかお確かめください。"
	#cursor.execute("INSERT INTO tipqueue (id, to, amount) VALUES (%s, %s, %s)", (userid, to, amount))
	#json = {
	#	"type": "tip",
	#	"to": "toaddress",
	#	"from": "fromaddress",
	#	"id": "00000000"
	#}
	#TODO:ってか下のやつゆくゆくはtoをMonage IDにしてクライアント側でアドレス照合したいなー

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
	string = string.replace(",", "")
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
connection.close()