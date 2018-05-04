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
import sqlite3
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
	address2 = address.replace('[', '')
	address3 = address2.replace(']', '')
	address4 = address3.replace('\n', '')
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	elapsed_time = time.time() - start
	elapsed_time = str(elapsed_time)
	return address4
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
	if amount >= "0.01":
		if amount >= balancea:
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
			m = "1"
	else:
		#m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
		m = "2"
	return m
