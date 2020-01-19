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
import urllib
import MySQLdb
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('/root/dismona.conf')

section1 = 'development'
walletpassphrase = config.get(section1, 'mona_walletpassphrase')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')
electrum_wallet_location = config.get(section1, 'electrum_wallet_location')
def userwalletlocation(userid):
	location = "" + electrum_wallet_location + "" + userid + ""
	return location
#MONAPARTY関連スタート
def balance(address):
	print("1")
	address = '"' + addresses + '"'
	print(addresses)
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Accept': 'application/json, text/javascript',
	}
	data = '{\
	"jsonrpc":"2.0",\
	"id":0,\
	"method":"get_normalized_balances",\
	"params":{\
	"addresses":[\
	' + addresses + '\
	]\
	}\
	}'
	print(data)
	response = requests.post('https://monapa.electrum-mona.org/_api', headers=headers, data=data, auth=('rpc', 'hello'))
	print(response)
	print(response.text)
	responsejson = response.json()
	responseresult = responsejson['result']
	if response.text is None:
		return "0-1" #No return fetched from server, possibilly server error.
	elif responseresult is None:
		return "0-2" #No token balance found.
	else:
		return responseresult


def deposit(userid):
	walletlocation = userwalletlocation(userid)
	cmdlib = "electrum-mona listaddresses -D {0}".format(walletlocation)
	rut  =  subprocess.check_output( cmd.split(" ") )
	address = rut.decode()
	address2 = address.replace('"', '')
	address3 = address2.replace(',', '')
	address = address3.split()
	address = address[1]
	address = address.replace(']', '')
	return address

def rawtransaction(userid, tipto, amount, tiptoken):
	#まず最初に数字を取り出す。次にWordを取り出し、とりだしたWordから数字を取り除く。
	print("")
	print(tipto)
	print(tipamount)
	print(tiptoken)
	print("")
	addresses = deposit(userid)
	address = addresses
	print(address)
	print(addresses)
	addresses = '"' + addresses + '"'
	tiptoaddress = deposit(tipto)
	tiptoaddress = '"' + tiptoaddress + '"'
	tiptoken = '"' + tiptoken + '"'
	#APIにアクセスし該当TXIDをもらってくる
	fee = "2000"

	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Accept': 'application/json, text/javascript',
	}

	data = '{"jsonrpc":"2.0", "id":0, "params":{"method":"get_asset_info", "params":{"assets":[' + tiptoken + ']} }'

	asset_info = requests.post('https://monapa.electrum-mona.org/_api ', headers=headers, data=data, auth=('rpc', 'rpc'))
	responsejson = asset_info.json()
	responseresult = responsejson['result']
	print(responseresult)
	isdivisible = responseresult[0]["divisible"]
	isdivisible = str(isdivisible)
	print(isdivisible)
	print("---Assetinfo compleate---")
	satoshivalue = "100000000"
	satoshivalue = int(satoshivalue)
	if isdivisible == "True":
		tipamount = float(tipamount)
		tipamount = tipamount * satoshivalue
		print(tipamount)
		tipamount = int(tipamount)
		tipamount = str(tipamount)
	data = '{"jsonrpc":"2.0","id":0,"method":"proxy_to_counterpartyd","params":{\n \
		"method": "create_send",\n \
		"params": {"source": ' + addresses + ', "destination": ' + tiptoaddress + ', "asset": ' + tiptoken + ', "quantity": ' + tipamount + ', "fee": ' + fee + ', "allow_unconfirmed_inputs": true, "use_enhanced_send": false }\n \
	}'
	print(data)
	repfrom = '"' + tipamount + '"'
	data = data.replace(repfrom, tipamount)
	print(data)
	response = requests.post('https://monapa.electrum-mona.org/_api', headers=headers, data=data, auth=('rpc', 'rpc'))
	print(response)
	print(response.text)
	print("---create_send request compleate---")
	print("")
	responsejson = response.json()
	rawtransaction = responsejson['result']
	print(rawtransaction)
	rawtransaction = str(rawtransaction)
	print("")
	return rawtransaction
def sign_raw_transaction(userid, rawtransaction):
	walletlocation = userwalletlocation(userid)
	cmd = "electrum-mona -D {0} signtransaction".format(walletlocation)
	rut  =  subprocess.check_output( cmd.split(" ") )
	result = rut.decode()
	return result
