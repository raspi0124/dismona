#!/usr/bin/python3
import discord
import subprocess
import re
import time
import math
import random
import json
import requests
import decimal
from decimal import (Decimal, ROUND_DOWN)
import apim
import sqlite3
from datetime import datetime

def round_down5(value):
	value = Decimal(value).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)
	return value

client = discord.Client()
currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# データベース接続とカーソル生成
# 接続情報はダミーです。お手元の環境にあわせてください。
#connection = MySQLdb.connect(
#   host='localhost', user='root', passwd='laksjd', db='dismona', charset='utf8')
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS dismona.id (id VARCHAR(20), address VARCHAR(50));")

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print(currenttime)
	print('------')
	await client.change_presence(game=discord.Game(name='/help'))


@client.event
async def on_message(message):
	dbpath = '/root/vote.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	towrite = "" + message.author.name + " said " + message.content + ". userid: " + message.author.id + " channel id: " + message.channel.id + " currenttime: " + currenttime + "\n"
	print(towrite)
	if message.content.startswith("/vote"):
			# データベース接続とカーソル生成
		username = message.author.id
		# エラー処理（例外処理）
		try:
		# INSERT
			cursor.execute("SELECT tokenamount FROM users WHERE id = " + username + "")
			amount = cursor.fetchall()
			print(amount)
			amount = str(amount)
			pattern = r'([0-9]+\.?[0-9]*)'
			amount = re.findall(pattern,amount)

			message = message.content
			message = re.findall(pattern,message)
			yesno = message[1]
			voteid = message[0]
			#yesno 1 is yes
			if amount != "":
				if yesno = "1":
					cursor.execute("SELECT yes FROM vote WHERE id = " + voteid + "")
					yesdamount = cursor.fetchall()
					print(yesdamount)
					yesdamount = str(yesdamount)
					pattern = r'([0-9]+\.?[0-9]*)'
					yesdamount = re.findall(pattern,yesdamount)
					yesdamount = yesdamount[0]
					yesamount = float(yesdamount) + float(amount)
					yesamount = str(yesamount)
					cursor.execute("UPDATE vote SET yes = " + yesamount + " WHERE id = " + voteid + "")
					m = "Success, voted for " + voteid+ " with answer of " + yesno + ""
				if yesno = "0":
					cursor.execute("SELECT no FROM vote WHERE id = " + voteid + "")
					nodamount = cursor.fetchall()
					print(nodamount)
					nodamount = str(nodamount)
					pattern = r'([0-9]+\.?[0-9]*)'
					nodamount = re.findall(pattern,nodamount)
					nodamount = nodamount[0]
					noamount = float(nodamount) + float(amount)
					noamount = str(noamount)
					cursor.execute("UPDATE vote SET no = " + noamount + " WHERE id = " + voteid + "")
					m = "Success, voted for " + voteid+ " with answer of " + yesno + ""
				await client.send_message(message.channel, m)
			else:
				m = "Not enough balance to take fee. Please note that fee of 0.01mona will be charged for registering rain.(only once.)"
				await client.send_message(message.channel, m)
		except sqlite3.Error as e:
			print('sqlite3.Error occurred:', e.args[0])
			m = "DB error. DB might locked. Please contact Izaya or raspi0124."
			await client.send_message(message.channel, m)

		if message.content.startswith("/createvote"):
			message = message.content
			pattern = r'([0-9]+\.?[0-9]*)'
			message = re.findall(pattern,message)
			voteid = message[0]
			try:
				cursor.execute("INSERT INTO vote (id) VALUES (?)", (voteid))
				m = "Created vote successfully with id of " + voteid + "."
			except sqlite3.Error as e:
				m = "DB error. DB might locked. Please contact Izaya or raspi0124."
			await client.send_message(message.channel, m)

		if message.content.startswith("/checkvote"):
			message = message.content
			pattern = r'([0-9]+\.?[0-9]*)'
			message = re.findall(pattern,message)
			voteid = message[0]
			cursor.execute("SELECT yes FROM vote WHERE id = " + voteid + "")
			yesamount = cursor.fetchall()
			print(yesamount)
			yesamount = str(yesamount)
			pattern = r'([0-9]+\.?[0-9]*)'
			yesamount = re.findall(pattern,yesamount)
			yesamount = yesamount[0]
			yesamount = str(yesamount)

			cursor.execute("SELECT no FROM vote WHERE id = " + voteid + "")
			noamount = cursor.fetchall()
			print(noamount)
			noamount = str(noamount)
			pattern = r'([0-9]+\.?[0-9]*)'
			noamount = re.findall(pattern,noamount)
			noamount = noamount[0]
			noamount = str(noamount)
			m = "Here is the detail for voteid " + voteid + "/n YES: " + yesamount + "/n NO:" + noamount + ""
			await client.send_message(message.channel, m)


		# 保存を実行（忘れると保存されないので注意）
		connection.commit()

		await client.send_message(message.channel, m)
client.run("NDA5MDkwMTE4OTU2MDg5MzQ0.DbzXyg.ILwObUEbsoQN5OIHxi0Ujw59m0g")
connection.close()
# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21
