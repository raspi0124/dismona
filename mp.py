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

#MONAPARTY関連スタート
def mp_balance(address):
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
	if response.text is None:
		return "0-1" #No return fetched from server, possibilly server error.
	responsejson = response.json()
	responseresult = responsejson['result']
	elif responseresult is None:
		return "0-2" #No token balance found.
	else:
		return responseresult

def mp_deposit(userid):
	#Change those to elecctrum one after.
	# メッセージを書きます
	address = mlibs.deposit(userid)
	return address

def mp_rawtransaction(userid, tipto, amount, tiptoken):
	#まず最初に数字を取り出す。次にWordを取り出し、とりだしたWordから数字を取り除く。
	print("")
	print(tipto)
	print(tipamount)
	print(tiptoken)
	print("")
	addresses = mp_deposit(userid)
	address = addresses
	print(address)
	print(addresses)
	addresses = '"' + addresses + '"'
	tiptoaddress = mp_deposit(tipto)
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
