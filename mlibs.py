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

config = configparser.ConfigParser()
config.read('dismona.conf')

section1 = 'development'
walletpassphrase = config.get(section1, 'mona_walletpassphrase')
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
def unlockwallet():
	time = "30"
	time = str(time)
	cmda = "monacoin-cli walletpassphrase {0} {1}".format(walletpassphrase, time)
	subprocess.check_output( cmda.split(" ") )

def libgetbalance(userid):
	unlockwallet()
	minconf = "60"
	cmdlib = "monacoin-cli getbalance {0} {1}".format(userid, minconf)
	rutlib = subprocess.check_output( cmdlib.split(" ") )
	balancelib = rutlib.decode()
	balancelib = float(balancelib)
	balancelib = str(balancelib)
	return balancelib

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

	balance = libgetbalance(userid)
	balance = float(balance)
	jpybalance = float(currentprice) * float(balance)
	balance = str(balance)
	jpybalance = str(jpybalance)
	return jpybalance

def deposit(userid):
	unlockwallet()
	cmd = "monacoin-cli getaddressesbyaccount {}".format(userid)
	rut  =  subprocess.check_output( cmd.split(" ") )
	address = rut.decode()
	address2 = address.replace('"', '')
	address3 = address2.replace(',', '')
	address = address3.split()
	address = address[1]
	address = address.replace(']', '')
	return address
def getunconfbalance(userid):
	unlockwallet()
	minconf = "0"
	cmdlib = "monacoin-cli getbalance {0} {1}".format(userid, minconf)
	rutlib = subprocess.check_output( cmdlib.split(" ") )
	balancelib = rutlib.decode()
	balancelib = float(balancelib)
	balancelib = str(balancelib)
	return balancelib
def withdraw(userid, to, amount):
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
	balance = libgetbalance(userid)
	num2 = 100000000
	balance = float(balance) * float(num2)
	amount = float(amount) * float(num2)
	minimumtip = "1"
	minimumtip = float(minimumtip)
	if amount <= balance:
		if amount >= minimumtip:
			if userid != to:
				if len(to) > 16:
					username = userid
					amount = float(amount) / float(num2)
					amount = str(amount)
					cmd2 = "monacoin-cli move " + userid + " " + to + " " + amount + ""
					subprocess.check_output( cmd2.split(" ") )
					#m = "<@" + message.author.id + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + " . exectime: " + elapsed_time + " sec)"
					m = "200"
					cursor.execute("INSERT INTO tiped (id) VALUES (%s)", (username,))
					cursor.execute("INSERT INTO tiped (id) VALUES (%s)", (to,))
					connection.commit()
				else:
					m = "e_sl"
			else:
				m = "e_s2"
		else:
			#m = m = "<@" + message.author.id + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
			m = "e_10"
	else:
	#m = "<@"+ message.author.id + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
		m = "e_en"
	return m

def fixselect(string):
	string = str(string)
	string = string.replace('(', '')
	string = string.replace(')', '')
	string = string.replace("b'", '')
	string = string.replace("'", '')
	string = string.replace(",,", ',')
	string = string.replace("[", '')
	string = string.replace("]", '')
	string = string.split(',')
	string = str(string)
	return string

def register(userid):
	cmd = "monacoin-cli getnewaddress " + userid + ""
	rut  =  subprocess.check_output( cmd.split(" ") )
	#cursor.execute("insert into dismona.id(id,address) values('message_author', address);")
	resultaddress = rut.decode()
	resultmore = resultaddress.replace('[', '')
	resultmore2 = resultmore.replace(']', '')
	resultmore3 = resultmore2.replace('"', '')
	resultmore4 = resultmore3.replace("\n", "")
	resultmore5 = resultmore4.replace(" ", "")
	cursor.execute("INSERT INTO addresses (username, address) VALUES (%s, %s)", (userid, resultmore5))
	connection.commit()
	return resultmore5

def getpubkey(address):
	cmd = "monacoin-cli validateaddress {}".format(address)
	print(cmd)
	rut  =  subprocess.check_output( cmd.split(" ") )
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
