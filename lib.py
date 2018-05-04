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

def getbalance(userid):
	global ruta
	global currentprice
	global balance
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
	elapsed_time = time.time() - start
	elapsed_time = str(elapsed_time)
	balance = str(balance)
	jpybalance = str(jpybalance)
	return balance
def getjpybalance(userid):
	global getjpybalance
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
	elapsed_time = time.time() - start
	elapsed_time = str(elapsed_time)
	balance = str(balance)
	jpybalance = str(jpybalance)
	return jpybalance