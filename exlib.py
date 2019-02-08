#!/usr/bin/python3
#こっちはelectrumxを使っていろいろやるやつ
import subprocess
import re
import time
import math
import random
import json
import requests
import decimal
from decimal import (Decimal, ROUND_DOWN)
#import apim
#import sqlite3
import urllib
import MySQLdb
from datetime import datetime
import configparser
import connectrum
import re, textwrap, asyncio, sys
from connectrum.client import StratumClient
from connectrum.svr_info import KnownServers, ServerInfo
from connectrum.utils import address_to_scripthash
from connectrum import ElectrumErrorResponse

config = configparser.ConfigParser()
config.read('dismona.conf')

section1 = 'development'
walletpassphrase = config.get(section1, 'mona_walletpassphrase')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')

def call_electrum(conn, method, *args):
	# call a method and format up the response nicely
	print("args")
	print(args)
	svr = ServerInfo("electrumx.tamami-foundation.org", "electrumx.tamami-foundation.org",
					ports=(("tcp"+str("50001")) if "50001" else "tcp"))
	conn = StratumClient()
	t = ''
	try:
		resp = conn.RPC(method, *args)
	except ElectrumErrorResponse as e:
		response, req = e.args
		t += "2-1"
		return t
	print("CALL_ELECTRUM REPONSE")
	print(resp)
	return resp
def get_user_address(userid):
	address = "M8VjBRRfiwfRGBZvWSGvrkLX4oTQ6Dy4uY" #とりあえずblankにしておくけどきちんとロジックを考えてdbから出すなりハッシュとかで出すなりすること!
	#上はとりあえずのテスト用
	return address
def round_down5(value):
	value = Decimal(value).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)
	return str(value)
def userwalletlocation(userid):
	location = "" + electrum_wallet_location + "" + userid + ""
	return location

def libgetbalance(userid):
	address = get_user_address(userid)
	sh = address_to_scripthash(address)
	method = "blockchain.scripthash.get_balance"
	conn = "electrumx.tamami-foundation.org" #connに何いれればいいのかよくわからないからとりあえずアドレスにしとく。あとで聞いたほうがいいかな
	res = call_electrum(conn, method, sh)
	print(res)
	if "2-1" in str(res):
		balance = "2-1"
		return balance
	else:
		return res

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
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	balance = str(balance)
	jpybalance = str(jpybalance)
	return jpybalance

def deposit(userid):
	walletlocation = userwalletlocation(userid)
	cmdlib = "electrum-mona listaddresses -{0}".format(walletlocation)
	rut  =  subprocess.check_output( cmdlib.split(" ") )
	address = rut.decode()
	address2 = address.replace('"', '')
	address3 = address2.replace(',', '')
	address = address3.split()
	address = address[1]
	address = address.replace(']', '')
	return address

def withdraw(userid, to, amount):

	balancea = libgetbalance(userid)
	fee = "0.005"
	reamount = float(amount) - float(fee)
	reamount = round_down5(reamount)
	reamount = str(reamount)
	minbalance = "0.01"
	minbalance = float(minbalance)
	minamount = "0.01"
	minamount = float(minamount)
	balancea = float(balancea)
	amount = float(amount)
	if amount >= minamount:
		if amount <= balancea:
			cmd = "monacoin-cli sendfrom {0} {1} {2}".format(userid, to, reamount)
			rut  =  subprocess.check_output( cmd.split(" ") )
			cmd = "monacoin-cli move {0} fee {1}".format(userid, fee)
			ruta  =  subprocess.check_output( cmd.split(" ") )
			rut = rut.decode()
			m = rut
			balancea = libgetbalance(userid)
			if balancea <= "0":
				defo = "0"
				amounttosendback = float(defo) - float(balancea)
				amounttosendback = str(amounttosendback)
				cmd = "monacoin-cli move fee {0} {1}".format(userid, amounttosendback)
				ruta  =  subprocess.check_output( cmd.split(" ") )

		else:
			#m = "<@" + userid + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"
			m = "500"
	else:
		#m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
		m = "500"
	return m
def tiptoken(userid, to, amount, tiptoken):
	pass
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
				username = userid
				amount = float(amount) / float(num2)
				amount = str(amount)
				cmd2 = "monacoin-cli move " + userid + " " + to + " " + amount + ""
				rut2  =  subprocess.check_output( cmd2.split(" ") )
				#m = "<@" + message.author.id + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + " . exectime: " + elapsed_time + " sec)"
				m = "200"
				cursor.execute("INSERT INTO tiped (id) VALUES (%s)", (username,))
				cursor.execute("INSERT INTO tiped (id) VALUES (%s)", (to,))
				connection.commit()
			else:
				m = "e_s"
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
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
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
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
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
