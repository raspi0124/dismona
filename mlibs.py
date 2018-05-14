#!/usr/bin/python3
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
import MySQLdb
from datetime import datetime

def libgetbalance(userid):
	cmdlib = "monacoin-cli walletpassphrase 0124 10"
	rutlib  =  subprocess.check_output( cmdlib.split(" ") )
	print(rutlib)
	cmdlib = "monacoin-cli getbalance " + userid + ""
	rutlib  =  subprocess.check_output( cmdlib.split(" ") )
	balancelib = rutlib.decode()
	balancelib = float(balancelib)
	currenttimelib = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	balancelib = str(balancelib)
	return balancelib

def libgetjpybalance(userid):
	cmda = "monacoin-cli walletpassphrase 0124 10"
	ruta  =  subprocess.check_output( cmda.split(" ") )
	print(ruta)
	headers = {
	'Accept': 'application/json',
	}
	response = requests.get('https://public.bitbank.cc/mona_jpy/ticker', headers=headers)
	print(response.json())
	response = response.json()
	data = response['data']
	currentprice = data['last']
	currentprice = str(currentprice)
	print("currentprice:" + currentprice + "")
	currentprice = float(currentprice)

	cmd = "monacoin-cli getbalance " + userid + ""
	rut  =  subprocess.check_output( cmd.split(" ") )
	balance = rut.decode()
	balance = float(balance)
	jpybalance = float(currentprice) * float(balance)
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	balance = str(balance)
	jpybalance = str(jpybalance)
	return jpybalance
def deposit(userid):
	start = time.time()
	cmda = "monacoin-cli walletpassphrase 0124 10"
	ruta  =  subprocess.check_output( cmda.split(" ") )
	print(ruta)
	cmd = "monacoin-cli getaddressesbyaccount " + userid + ""
	rut  =  subprocess.check_output( cmd.split(" ") )
	address = rut.decode()
	address2 = address.replace('"', '')
	address3 = address2.replace(',', '')
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	elapsed_time = time.time() - start
	elapsed_time = str(elapsed_time)
	address = address3.split()
	print(address)
	address = address[1]
	return address
def withdraw(userid, to, amount):
	start = time.time()
	cmda = "monacoin-cli walletpassphrase 0124 10"
	ruta  =  subprocess.check_output( cmda.split(" ") )
	print(ruta)
	balancea = libgetbalance(userid)
	fee = "0.005"
	reamount = float(amount) - float(fee)
	reamount = str(reamount)
	print("--to--")
	print(to)
	print("--amount--")
	print(amount)
	print("--reamount--")
	print(reamount)
	minbalance = "0.01"
	minbalance = float(minbalance)
	minamount = "0.01"
	minamount = float(minamount)
	balancea = float(balancea)
	amount = float(amount)
	if amount >= minamount:
		if amount <= balancea:
			cmd = "monacoin-cli sendfrom " + userid + " " + to + " " + reamount + ""
			rut  =  subprocess.check_output( cmd.split(" ") )
			cmd = "monacoin-cli move " + userid + " fee " + fee + ""
			ruta  =  subprocess.check_output( cmd.split(" ") )
			print(rut)
			rut = rut.decode()
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
			m = rut
			balancea = libgetbalance(userid)
			if balancea <= "0":
				defo = "0"
				amounttosendback = float(defo) - float(balancea)
				print("--amounttosendback--")
				print(amounttosendback)
				amounttosendback = str(amounttosendback)
				cmd = "monacoin-cli move fee "  + userid + " " + amounttosendback + ""
				ruta  =  subprocess.check_output( cmd.split(" ") )
				print(ruta)

		else:
			#m = "<@" + userid + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"
			m = "500"
	else:
		#m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
		m = "500"
	return m

def tip(userid, to, amount):
	connection = MySQLdb.connect(db='dismona',user='root',passwd='laksjd',charset='utf8mb4')
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	balance = libgetbalance(userid)
	num2 = 100000000
	balance = float(balance) * float(num2)
	print ("balance")
	print(balance)
	print("amount")
	print(amount)
	amount = float(amount) * float(num2)
	print("multiplyed amount")
	print(amount)
	minimumtip = "1"
	minimumtip = float(minimumtip)
	if amount <= balance:
		if amount >= minimumtip:
			username = userid
			amount = float(amount) / float(num2)
			amount = str(amount)
			cmd2 = "monacoin-cli move " + userid + " " + to + " " + amount + ""
			rut2  =  subprocess.check_output( cmd2.split(" ") )
			#m = "<@" + message.author.id + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + " . exectime: " + elapsed_time + " sec)"
			m = "200"
			cursor.execute("INSERT INTO tiped (id) VALUES (?)", (username,))
			cursor.execute("INSERT INTO tiped (id) VALUES (?)", (to,))
			connection.commit()
		else:
			#m = m = "<@" + message.author.id + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
			m = "e_10"
	else:
	#m = "<@"+ message.author.id + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
		m = "e_en"
	return m
