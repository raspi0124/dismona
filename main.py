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
#import apim
import sqlite3
from datetime import datetime
import mlibs

def round_down5(value):
	value = Decimal(value).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)
	return value

client = discord.Client()
currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

print("0101")
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
async def on_reaction_add(reaction, user):
	dbpath = '/root/dismona.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	'''
	print("reaction has been added")
	print(reaction)
	print("message")
	print(reaction.message)
	print("emoji")
	print(reaction.emoji)
	print("reaction-channel")
	print(reaction.message.channel)
	print("reaction-channel-id")
	print(reaction.message.channel.id)
	print("message-content")
	print(reaction.message.content)
	print("message-author")
	print(reaction.message.author.id)
	print("reaction-by")
	print(user.id)
	print("emoji-hash")
	print(hash(reaction.emoji))
	print("emoji-name")
	print(reaction.emoji.name)
	print("emoji-id")
	print(reaction.emoji.id)
	'''
	tipto = reaction.message.author.id
	tipby = user.id
	emoji = reaction.emoji.name
	tip0114114 = "monage0114114"
	tip039 = "monage039"
	if emoji == tip0114114:
		cmda = "monacoin-cli walletpassphrase 0124 10"
		ruta  =  subprocess.check_output( cmda.split(" ") )
		print(ruta)
		currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		cmd = "monacoin-cli getbalance " + tipby + ""
		rut  =  subprocess.check_output( cmd.split(" ") )
		balance = rut.decode()
		num2 = 100000000
		balance = float(balance) * float(num2)
		print ("balance")
		print(balance)
		tipamount = "0.114114"
		print("tipamount")
		print(tipamount)
		tipamount = float(tipamount) * float(num2)
		print("multiplyed tipamount")
		print(tipamount)
		minimumtip = "1"
		minimumtip = float(minimumtip)
		if tipamount <= balance:
			if tipamount >= minimumtip:
				try:
					username = tipby
					tipamount = float(tipamount) / float(num2)
					tipamount = str(tipamount)
					cmd2 = "monacoin-cli move " + tipby + " " + tipto + " " + tipamount + ""
					rut2  =  subprocess.check_output( cmd2.split(" ") )
					m = "<@" + tipby + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
					await client.send_message(reaction.message.channel, m)
					cursor.execute("INSERT INTO tiped (id) VALUES (?)", (username,))
					connection.commit()
					cursor.execute("INSERT INTO tiped (id) VALUES (?)", (tipto,))
				except subprocess.CalledProcessError as e:
					eout = e.output.decode()
					m = "<@" + tipby + ">, sorry, failed to complete your request: <@" + tipto + "> is not yet registered.\n(message created on " + currenttime + ")"
					await client.send_message(reaction.message.channel, m)
			else:
				m = "<@" + tipby + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
				await client.send_message(reaction.message.channel, m)
		else:
			m = "<@"+ tipby + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
			await client.send_message(reaction.message.channel, m)

	if emoji == tip039:
		cmda = "monacoin-cli walletpassphrase 0124 10"
		ruta  =  subprocess.check_output( cmda.split(" ") )
		print(ruta)
		currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		cmd = "monacoin-cli getbalance " + tipby + ""
		rut  =  subprocess.check_output( cmd.split(" ") )
		balance = rut.decode()
		num2 = 100000000
		balance = float(balance) * float(num2)
		print ("balance")
		print(balance)
		tipamount = "0.39"
		print("tipamount")
		print(tipamount)
		tipamount = float(tipamount) * float(num2)
		print("multiplyed tipamount")
		print(tipamount)
		minimumtip = "1"
		minimumtip = float(minimumtip)
		if tipamount <= balance:
			if tipamount >= minimumtip:
				try:
					username = tipby
					tipamount = float(tipamount) / float(num2)
					tipamount = str(tipamount)
					cmd2 = "monacoin-cli move " + tipby + " " + tipto + " " + tipamount + ""
					rut2  =  subprocess.check_output( cmd2.split(" ") )
					m = "<@" + tipby + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
					await client.send_message(reaction.message.channel, m)
					cursor.execute("INSERT INTO tiped (id) VALUES (?)", (username,))
					connection.commit()
					cursor.execute("INSERT INTO tiped (id) VALUES (?)", (tipto,))
				except subprocess.CalledProcessError as e:
					eout = e.output.decode()
					m = "<@" + tipby + ">, sorry, failed to complete your request: <@" + tipto + "> is not yet registered.\n(message created on " + currenttime + ")"
					await client.send_message(reaction.message.channel, m)
			else:
				m = "<@" + tipby + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
				await client.send_message(reaction.message.channel, m)
		else:
			m = "<@"+ tipby + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
			await client.send_message(reaction.message.channel, m)

@client.event
async def on_message(message):
	import mlibs
	dbpath = '/root/dismona.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	cursor.execute('SELECT * FROM agreetos')
	agreetos = cursor.fetchall()
	agreetos = str(agreetos)
	pattern = r'([0-9]+\.?[0-9]*)'
	agreetos = re.findall(pattern,agreetos)
	userid = message.author.id
	messagesql = message.content.encode('utf-8')
	messagesql = str(messagesql)
	useird = message.author.id	
	if message.content.startswith("/"):
		towrite = "" + message.author.name + " said " + messagesql + ". userid: " + message.author.id + " channel id: " + message.channel.id + " currenttime: " + currenttime + "\n"
		file = open('/root/alllog2.txt', 'a')  #追加書き込みモードでオープン
		file.writelines(towrite)
		print(towrite)
		#cursor.execute("INSERT INTO log (author, message, userid, channelid, currenttime) VALUES (?, ?, ?, ?, ?)", (message.author.name, message, message.author.id, message.channel.id, currenttime))
		#connection.commit()
	rainnotify = "425766935825743882"
	rainnotify = client.get_channel('425766935825743882')

	if message.content.startswith("/") and message.content != "/agreetos" and message.content != "/cagreedtos" and message.content != "/help" and userid in agreetos:
		# 全件取得は cursor.fetchall()
		# 「/register」で始まるか調べる

		if message.content.startswith("/register"):
			start = time.time()
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			await client.add_reaction(message, '👌')
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
				# メッセージを書きます
				m = "<@" + message.author.id + "> さんのアカウントを作成しますね！"
				# メッセージが送られてきたチャンネルへメッセージを送ります
				await client.send_message(message.channel, m)
				cmd = "monacoin-cli getnewaddress " + message.author.id + ""
				rut  =  subprocess.check_output( cmd.split(" ") )
				print ('Creating <' + message.author.id + ">s account.. user ID ")
				#cursor.execute("insert into dismona.id(id,address) values('message_author', address);")
				resultaddress = rut.decode()
				resultmore = resultaddress.replace('[', '')
				resultmore2 = resultmore.replace(']', '')
				resultmore3 = resultmore2.replace('"', '')
				resultmore4 = resultmore3.replace("\n", "")
				resultmore5 = resultmore4.replace(" ", "")
				cursor.execute("INSERT INTO addresses (username, address) VALUES (?, ?)", (username, resultmore5))
				currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
				elapsed_time = time.time() - start
				elapsed_time = str(elapsed_time)
				m = "<@" + message.author.id + ">, successfully created an account for you! Your new address is " + resultmore5 + ", enjoy!\n(message created on " + currenttime + " exectime: " + elapsed_time + " sec)"
				await client.send_message(message.channel, m)
				connection.commit()

		if message.content.startswith("/rera"):
			start = time.time()
				# データベース接続とカーソル生成
			username = message.author.id
			# エラー処理（例外処理）
			try:
			# INSERT
				cmd = "monacoin-cli getbalance " + username + ""
				rut  =  subprocess.check_output( cmd.split(" ") )
				balance = rut.decode()
				if balance > "0.01":
					fee = "0.01"
					cursor.execute("INSERT INTO rainregistered (rainid) VALUES (?)", (username,))
					cmd = "monacoin-cli move "  + message.author.id + " fee " + fee + ""
					ruta  =  subprocess.check_output( cmd.split(" ") )
					print(ruta)
					m = "Success. exectime: " + elapsed_time + " sec"
					await client.send_message(message.channel, m)
				else:
					m = "Not enough balance to take fee. Please note that fee of 0.01mona will be charged for registering rain.(only once.)"
					await client.send_message(message.channel, m)
			except sqlite3.Error as e:
				print('sqlite3.Error occurred:', e.args[0])
				m = "DB error. DB might locked or you already signed up."
				await client.send_message(message.channel, m)

			# 保存を実行（忘れると保存されないので注意）
			connection.commit()

		if message.content.startswith("/balance"):
			await client.add_reaction(message, '👌')
			m = "<@" + message.author.id + "> さんの残高チェック中.."
		# メッセージが送られてきたチャンネルへメッセージを送ります
			await client.send_message(message.channel, m)
			balance = mlibs.libgetbalance(userid)
			jpybalance = mlibs.libgetjpybalance(userid)
			m = "<@" + message.author.id + ">, you currently have  " + balance + " mona! (" + jpybalance + " jpy)\n(message created on " + currenttime + ")"
			print ("---6---")
			await client.send_message(message.channel, m)

		if message.content.startswith("/deposit"):
			await client.add_reaction(message, '👌')
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
			# メッセージを書きます
				m = "<@" + message.author.id + "> アドレスを確認中..."
			# メッセージが送られてきたチャンネルへメッセージを送ります
				await client.send_message(message.channel, m)
				address3 = mlibs.deposit(userid)
				m = "<@" + message.author.id + ">, the following are your deposit addresses:" + address3 + "\n(message created on " + currenttime + ")"
				await client.send_message(message.channel, m)
		if message.content.startswith("/list"):
			await client.add_reaction(message, '👌')
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
			# メッセージを書きます
				m = "<@" + message.author.id + "> アドレスを確認中..."
			# メッセージが送られてきたチャンネルへメッセージを送ります
				await client.send_message(message.channel, m)
				address3 = mlibs.deposit(userid)
				m = "<@" + message.author.id + ">, the following are your deposit addresses:" + address3 + "\n(message created on " + currenttime + ")"
				await client.send_message(message.channel, m)
		if message.content.startswith("/withdraw"):
			await client.add_reaction(message, '👌')
			rmessage = message.content.replace('/withdraw', '')
			print(rmessage)
			pattern = r'([+-]?[0-9]+\.?[0-9]*)'
			print(re.findall(pattern,rmessage))
			withdrawinfo = re.findall(pattern,rmessage)
			print(withdrawinfo[0])
			amount = withdrawinfo[0]
			rmessage = rmessage.replace(amount, '')
			to = rmessage.replace(' ', '')
			withdraw_detail = mlibs.withdraw(userid, to, amount)

			if withdraw_detail == "1":
				m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
			if withdraw_detail == "2":
				m = "<@" + userid + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"
			if withdraw_detail == "3":
				m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
			else:
				m = "Withdraw successfull. TXID:" + withdraw_detail + ""
			await client.send_message(message.channel, m)
		if message.content.startswith("/rain"):
			start = time.time()
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			cmda = "monacoin-cli getbalance " + message.author.id + ""
			ruta  =  subprocess.check_output( cmda.split(" ") )
			balancea = ruta.decode()
			await client.add_reaction(message, '👌')
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			message2 = message.content.replace('/rain ', '')
			pattern = r'([+-]?[0-9]+\.?[0-9]*)'
			raininfo = re.findall(pattern,message2)
			print("--numbertorain--")
			print(raininfo[0])
			print("--amounttorain--")
			print(raininfo[1])
			sum = float(raininfo[1]) / float(raininfo[0])
			print(sum)
			sum = round(sum,6)
			print(sum)
			sum = str(sum)
			cursor.execute('SELECT * FROM rainregistered ORDER BY rainid')

			# 全件取得は cursor.fetchall()
			rainall = cursor.fetchall()
			print(rainall)
			rainall = str(rainall)
			pattern = r'([0-9]+\.?[0-9]*)'
			rainall = re.findall(pattern,rainall)
			print(rainall)
			if balancea >= raininfo[1]:
				if raininfo[1] > "0.01":
					if sum > "0.001":
						m = "you will rain " + sum + "mona to " + raininfo[0] + " people."
						await client.send_message(message.channel, m)
						sum = str(sum)
						numbertosend = raininfo[0]
						numbertosend = int(numbertosend)
						maxrain = len(rainall)
						print(maxrain)
						m = "Rain started by <@" + message.author.id + "> at #" + message.channel.name + ""
						await client.send_message(rainnotify, m)
						for var in range(0, numbertosend):
							tosend = random.randrange(maxrain)
							print(tosend)
							print("--rondomfinish--")
							tosend = int(tosend)
							tosend = rainall[tosend]
							tosend = str(tosend)
							print("--startcommand--")
							cmd = "monacoin-cli move " + message.author.id + " " + tosend + " " + sum + ""
							rut  =  subprocess.check_output( cmd.split(" ") )
							print(rut)
							m = "Raining" + sum + "mona to <@" + tosend + ">.."
							await client.send_message(rainnotify, m)
						m = "finished raining " + sum + "mona to " + raininfo[0] + "people! total amount was " + raininfo[1] + "mona! Rained by <@" + message.author.id + ">"
						await client.send_message(message.channel, m)
						m = "finished raining " + sum + "mona to " + raininfo[0] + "people! total amount was " + raininfo[1] + "mona! Rained by <@" + message.author.id + ">"
						await client.send_message(rainnotify, m)
						print(rut)
					else:
						m = "負荷軽減のため1人当たりのrainが0.001mona以下になるrainは制限しています。"
				else:
					m = "Due to Server load, it is not allowed to make total amount of rain less then 0.01."
					await client.send_message(message.channel, m)
			else:
				m = "not enough fund.. double check amount to rain."
				await client.send_message(message.channel, m)
		if message.content.startswith("/ban"):
			start = time.time()
			username = message.author.id
			banallow = ["326091178984603669", "294470458013908992"]
			noban = ["326091178984603669", "294470458013908992"]
			if username in banallow:
				message2 = message.content
				pattern = r'([+-]?[0-9]+\.?[0-9]*)'
				tipinfo = re.findall(pattern,message2)
				print(tipinfo[0])
				banto = tipinfo[0]
				if banto not in noban:
					cursor.execute("INSERT INTO baned (banedid) VALUES (?)", (banto,))
					connection.commit()
					cursor.execute("INSERT INTO baned (banfromid) VALUES (?)", (username,))
					m = "<@" + username + ">ユーザー <@" + banto + "> をおみくじの使用からBANしました。"
					await client.send_message(message.channel, m)
				else:
					m = "このユーザーをBANすることは禁止されています。"
			else:
				m = "You are not allowed to do that!"
				await client.send_message(message.channel, m)

		if message.content.startswith("/tip"):
			start = time.time()
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			message2 = message.content.replace('/tip', '')
			print (message2)
			pattern = r'([+-]?[0-9]+\.?[0-9]*)'
			print(re.findall(pattern,message2))
			tipinfo = re.findall(pattern,message2)
			print(tipinfo[0])
			print(tipinfo[1])
			cmd = "monacoin-cli getbalance " + message.author.id + ""
			rut  =  subprocess.check_output( cmd.split(" ") )
			balance = rut.decode()
			num2 = 100000000
			balance = float(balance) * float(num2)
			print ("balance")
			print(balance)
			tipto = tipinfo[0]
			tipamount = tipinfo[1]
			print("tipamount")
			print(tipamount)
			tipamount = float(tipamount) * float(num2)
			print("multiplyed tipamount")
			print(tipamount)
			minimumtip = "1"
			minimumtip = float(minimumtip)
			if tipamount <= balance:
				if tipamount >= minimumtip:
					try:
						username = message.author.id
						tipamount = float(tipamount) / float(num2)
						tipamount = str(tipamount)
						cmd2 = "monacoin-cli move " + message.author.id + " " + tipto + " " + tipamount + ""
						rut2  =  subprocess.check_output( cmd2.split(" ") )
						elapsed_time = time.time() - start
						elapsed_time = str(elapsed_time)
						m = "<@" + message.author.id + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + " . exectime: " + elapsed_time + " sec)"
						await client.send_message(message.channel, m)
						cursor.execute("INSERT INTO tiped (id) VALUES (?)", (username,))
						connection.commit()
						cursor.execute("INSERT INTO tiped (id) VALUES (?)", (tipto,))
					except subprocess.CalledProcessError as e:
						eout = e.output.decode()
						m = "<@" + message.author.id + ">, sorry, failed to complete your request: <@" + tipto + "> is not yet registered.\n(message created on " + currenttime + ")"
						await client.send_message(message.channel, m)
				else:
					m = "<@" + message.author.id + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
					await client.send_message(message.channel, m)
			else:
				m = "<@"+ message.author.id + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
				await client.send_message(message.channel, m)
		if message.content.startswith("/admin info"):
			start = time.time()
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			await client.add_reaction(message, '👌')
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			cmd = "monacoin-cli getinfo"
			rut  =  subprocess.check_output( cmd.split(" ") )
			cmd2 = "monacoin-cli getbalance"
			rut2 = subprocess.check_output( cmd2.split(" "))
			cmd3 = "monacoin-cli listaccounts"
			rut3 = subprocess.check_output( cmd3.split(" "))
			cmd4 = "monacoin-cli listtransactions"
			rut4 = subprocess.check_output( cmd4.split(" "))
			getinfo = rut.decode()
			getbalance = rut2.decode()
			listaccounts = rut3.decode()
			listtransactions = rut4.decode()
			if message.author.id == "326091178984603669":
				m = "Verfifying.. wait a monemt"
				await client.send_message(message.channel, m)
				m = "Successfully verified you as an admin, here is the info you requested:"
				await client.send_message(message.channel, m)
				m = "```getinfo result: " + getinfo + "\n```"
				await client.send_message(message.channel, m)
				time.sleep(1)
				m = "```getbalance result: " + getbalance + "\n```"
				await client.send_message(message.channel, m)
				time.sleep(1)
				m = "```listaccounts result: " + listaccounts + "\n```"
				await client.send_message(message.channel, m)
				time.sleep(1)
				m = "```listtransactions result: " + listtransactions +"\n ```"
				await client.send_message(message.channel, m)
				time.sleep(1)
			else:
				m = "Haha, you don't have permission to do that! Your request has been logged and reported to the admin! (but the admin probably won't care about it, so don't worry.)"
				await client.send_message(message.channel, m)
		if message.content.startswith("/adminc"):
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			if message.author.id == "326091178984603669":
				message2 = message.content.replace('/adminc', '')
				print(message2)
				cmd = "monacoin-cli" + message2 + ""
				rut = subprocess.check_output( cmd.split(" "))
				result = rut.decode()
				await client.send_message(message.channel, result)
				await client.add_reaction(message, '👌')
			else:
				m = "sorry, but you are not allowed to do that!"
				await client.send_message(message.channel, m)
		if message.content.startswith('/members'):
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			await client.add_reaction(message, '👌')
			for server in client.servers:
				for member in server.members.id:
					print (member)
					list_of_ids = [m.id  for m in server.members]
					print(list_of_ids)
		if message.content.startswith('/adminregister'):
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			await client.add_reaction(message, '👌')
			if message.author.id == "326091178984603669":
				message2 = message.content.replace('/adminregister', '')
				message3 = message2.replace(' ', '')
				print(message3)
				cmd = "monacoin-cli getnewaddress " + message3 + ""
				rut = subprocess.check_output( cmd.split(" "))
				address = rut.decode()
				m = "issued account for <@" + message3 + ">. address is " + address + "."
				await client.send_message(message.channel, m)
			else:
				m = "sorry, but you are not allowed to do that!"
				await client.send_message(message.channel, m)
		if message.content.startswith('/adminbalance'):
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
			await client.add_reaction(message, '👌')
			if message.author.id == "326091178984603669":
				message2 = message.content.replace('/adminbalance', '')
				message3 = message2.replace(' ', '')
				print(message3)
				cmd = "monacoin-cli getbalance " + message3 + ""
				rut = subprocess.check_output( cmd.split(" "))
				balance = rut.decode()
				m = "<@" + message3 + "> 's balance are " + balance + "mona."
				await client.send_message(message.channel, m)
			else:
				m = "sorry, but you are not arrowed to do that!"
				await client.send_message(message.channel, m)
		if message.content.startswith("/image"):
			await client.add_reaction(message, '👌')
			with open('../image.png', 'rb') as f:
				await client.send_file(message.channel, f)
		if message.content.startswith("/hello"):
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			start = time.time()
			m = "こんにちは! <@" + message.author.id + "> さん！"
			await client.send_message(message.channel, m)
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
			m = "elapsed time:" + elapsed_time + "sec"
			await client.send_message(message.channel, m)
			await client.add_reaction(message, '👌')
		if message.content.startswith("/rmomikuzi"):
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			start = time.time()
			if message.author.id == "326091178984603669":
				cmd = "sh dismona-rm.sh"
				ruta  =  subprocess.check_output( cmd.split(" ") )
				print(ruta)
				m = "True"
				await client.send_message(message.channel, m)
				elapsed_time = time.time() - start
				elapsed_time = str(elapsed_time)
				m = "elapsed time:" + elapsed_time + "sec"
				await client.send_message(message.channel, m)
				await client.add_reaction(message, '👌')
		if message.content.startswith("/love"):
			start = time.time()
			username = message.author.id
			cursor.execute('SELECT * FROM loved')
			loved = cursor.fetchall()
			print(loved)
			loved = str(loved)
			pattern = r'([0-9]+\.?[0-9]*)'
			loved = re.findall(pattern,loved)
			cmd = "monacoin-cli getbalance " + message.author.id + ""
			rut  =  subprocess.check_output( cmd.split(" ") )
			balance = rut.decode()
			print(balance)
			balance = str(balance)
			print(balance)
			balance = re.findall(pattern,balance)
			balance = balance[0]
			print(balance)
			balance = float(balance)
			if message.author.id == "406829226751295488":
				m = "友達にもなりたくないです。二度と話しかけないでください"
				await client.send_message(message.channel, m)
			else:
				if username not in loved:
					minbal = "1"
					minbal = int(minbal)

					if balance >= minbal:
						def love():
							kuji = ["0", "1", "2", "3", "1", "2", "7", "1", "2", "3", "1", "2", "3", "2", "3", "2", "0", "0"]
							result = random.choice(kuji)
							return result
						kuji = ["うーん。。お断りさせていただきます", "お友達から初めましょう", "。。。", "お友達から初めましょう。", "あなたのことなんか大っ嫌い!", "お友達で居ましょう。", "うーん。。お断りさせていただきます", "結婚してください！大好きです！"]
						result = love()
						print("result")
						print(result)
						result = int(result)
						m = kuji[result]
						print("m")
						print(m)
						loven = "7"
						loven = int(loven)
						if result == loven:
							cursor.execute("INSERT INTO loved (id) VALUES (?)", (username,))
							connection.commit()
						await client.send_message(message.channel, m)
						elapsed_time = time.time() - start
						elapsed_time = str(elapsed_time)
						m = ". exectime: " + elapsed_time + " sec"
						await client.send_message(message.channel, m)
						await client.delete_message(message)
					else:
						m = "私お金のない人と付き合いたくないのよ。ごめんなさいね。"
						await client.send_message(message.channel, m)

				else:
					def loved():
						kuji = ["0", "1", "2"]
						result = random.choice(kuji)
						return result
					messeages = ["私も愛してるわよ。ダーリン。", "あなたのこと、大好きよ。", "実家に帰らさせていただきます！"]
					result = loved()
					result = int(result)
					m = messeages[result]
					await client.send_message(message.channel, m)
					lovedn = "2"
					lovedn = int(lovedn)
					username = '"' + username + '"'
					if result == lovedn:
						cursor.execute("DELETE FROM loved WHERE id = " + username + "")
						connection.commit()
					await client.delete_message(message)
			if message.content.startswith("/marryhim"):
				if message.author.id == "326091178984603669":
					username = message.author.id
					cursor.execute('SELECT * FROM loved')
					loved = cursor.fetchall()
					print(loved)
					loved = str(loved)
					pattern = r'([0-9]+\.?[0-9]*)'
					loved = re.findall(pattern,loved)
					message = message.content
					tolove = re.findall(pattern,message)
					tolove = tolove[0]
					if message.author.id == "aaa":
						m = "友達にもなりたくないです。二度と話しかけないでください"
						await client.send_message(message.channel, m)
					else:
						if tolove not in loved:
							result = "1"
							loven = "1"
							m = "これもお家のため。。了解いたしました。たいへん不本意ですが <@" + tolove + "> と結婚させていただきます"
							if result == loven:
								cursor.execute("INSERT INTO loved (id) VALUES (?)", (tolove,))
								connection.commit()
							await client.send_message(message.channel, m)
						else:
							def loved():
								kuji = ["0"]
								result = random.choice(kuji)
								return result
							messeages = ["すでにあの方と結婚していますが何か?"]
							result = loved()
							result = int(result)
							m = messeages[result]
							await client.send_message(message.channel, m)

		if message.content == "/omikuzi -nomona" or message.content == "/omikuji -nomona":
			start = time.time()
			username = message.author.id
			cursor.execute('SELECT id FROM gived')
			# 全件取得は cursor.fetchall()
			gived = cursor.fetchall()
			print("gived")
			print(gived)
			gived = str(gived)
			cursor.execute('SELECT banedid FROM baned')
			baned = cursor.fetchall()
			cursor.execute('SELECT * FROM tiped')
			tiped = cursor.fetchall()
			print(tiped)
			tiped = str(tiped)
			pattern = r'([0-9]+\.?[0-9]*)'
			tiped = re.findall(pattern,tiped)
			print("banned")
			print(baned)
			print("tiped")
			print(tiped)
			baned = str(baned)
			await client.add_reaction(message, '👌')
			cursor.execute('SELECT * FROM loved')
			loved = cursor.fetchall()
			print(loved)
			loved = str(loved)
			pattern = r'([0-9]+\.?[0-9]*)'
			loved = re.findall(pattern,loved)

			if username not in gived:
				if username not in loved:
					def omikuji():
						kuji = ["0", "1", "2", "3", "1", "2", "7", "1", "2", "3", "1", "2", "3", "2", "3", "2", "0", "0"]
						result = random.choice(kuji)
						return result
					kuji = ["凶", "小吉", "中吉", "大吉", "凶", "小吉", "中吉", "超大吉"]
					result = omikuji()
					print("result")
					print(result)
					addamount = "1"
					result = int(result)
					resultp = kuji[result]
					result2 = float(result) + float(addamount)
					result2 = int(result2)
					print("resultp")
					print(resultp)
					resultp = str(resultp)
					result2 = int(result2)
					result2 = str(result2)
					result = str(result)
					a = "a"
					if a == a:
						if result == "0":
							with open('/root/dismona/kyou.png', 'rb') as f:
								await client.send_file(message.channel, f)
						if result == "1":
							with open('/root/dismona/syoukiti.png', 'rb') as f:
								await client.send_file(message.channel, f)
						if result == "2":
							with open('/root/dismona/tyuukiti.png', 'rb') as f:
								await client.send_file(message.channel, f)
						if result == "3":
							with open('/root/dismona/daikiti.png', 'rb') as f:
								await client.send_file(message.channel, f)
						if result == "7":
							with open('/root/dismona/tyoudaikiti.png', 'rb') as f:
								await client.send_file(message.channel, f)
					elapsed_time = time.time() - start
					elapsed_time = str(elapsed_time)
					resultp = str(resultp)
					m = "貴方の今日の運勢は" + resultp + "です!"
					await client.send_message(message.channel, m)
					cursor.execute("INSERT INTO gived (id) VALUES (?)", (username,))
					connection.commit()
				else:
					def omikuji():
						kuji = ["0", "1", "2", "3", "2", "4"]
						result = random.choice(kuji)
						return result
					kuji = ["凶", "小吉", "中吉", "大吉", "超大吉"]
					result = omikuji()
					print("result")
					print(result)
					result = int(result)
					print("resulta")
					print(result)
					resultp = kuji[result]
					print("resultp")
					print(resultp)
					resultp = str(resultp)
					result = float(result) + float("3")
					result = int(result)
					result = str(result)
					kyou = "0"
					kyou = int(kyou)
					elapsed_time = time.time() - start
					elapsed_time = str(elapsed_time)
					if result == kyou:
						m = "あなたの運勢…凶みたいだから、今日はそばにいてあげるんだからねっ！今日だけだからねっ"
					else:
						m = "ダーリン、あなたの今日の運勢は" + resultp + "らしいですわよ。! 今日も気をつけてね、ダーリン。 . exectime: " + elapsed_time + " sec"
					await client.send_message(message.channel, m)
					cursor.execute("INSERT INTO gived (id) VALUES (?)", (username,))
					m = "/tip <@" + username + "> 0.000" + result + ""
					await client.send_message(message.channel, m)
					connection.commit()
			else:
				m = "すでに今日におみくじをされているようです。。明日戻ってきてね！"
				await client.send_message(message.channel, m)

		if message.content == "/omikuzi" or message.content == "/omikuji":
			start = time.time()
			username = message.author.id
			cursor.execute('SELECT id FROM gived')
			# 全件取得は cursor.fetchall()
			gived = cursor.fetchall()
			print("gived")
			print(gived)
			gived = str(gived)
			cursor.execute('SELECT banedid FROM baned')
			baned = cursor.fetchall()
			cursor.execute('SELECT * FROM tiped')
			tiped = cursor.fetchall()
			print(tiped)
			tiped = str(tiped)
			pattern = r'([0-9]+\.?[0-9]*)'
			tiped = re.findall(pattern,tiped)
			print("banned")
			print(baned)
			print("tiped")
			print(tiped)
			baned = str(baned)
			cmd = "monacoin-cli getbalance " + username + ""
			balance = subprocess.check_output( cmd.split(" "))
			minlimit = "0.001"
			balance = str(balance)
			balance = re.findall(pattern,balance)
			await client.add_reaction(message, '👌')
			cursor.execute('SELECT * FROM loved')
			loved = cursor.fetchall()
			print(loved)
			loved = str(loved)
			pattern = r'([0-9]+\.?[0-9]*)'
			loved = re.findall(pattern,loved)

			if username not in gived:
				if username not in baned:
					if username in tiped:
						if username not in loved:
							def omikuji():
								kuji = ["0", "1", "2", "3", "1", "2", "7", "1", "2", "3", "1", "2", "3", "2", "3", "2", "0", "0"]
								result = random.choice(kuji)
								return result
							kuji = ["凶", "小吉", "中吉", "大吉", "凶", "小吉", "中吉", "超大吉"]
							result = omikuji()
							print("result")
							print(result)
							addamount = "1"
							result = int(result)
							resultp = kuji[result]
							result2 = float(result) + float(addamount)
							result2 = int(result2)
							print("resultp")
							print(resultp)
							resultp = str(resultp)
							result2 = int(result2)
							result2 = str(result2)
							result = str(result)
							a = "a"
							if a == a:
								if result == "0":
									with open('/root/dismona/kyou.png', 'rb') as f:
										await client.send_file(message.channel, f)
								if result == "1":
									with open('/root/dismona/syoukiti.png', 'rb') as f:
										await client.send_file(message.channel, f)
								if result == "2":
									with open('/root/dismona/tyuukiti.png', 'rb') as f:
										await client.send_file(message.channel, f)
								if result == "3":
									with open('/root/dismona/daikiti.png', 'rb') as f:
										await client.send_file(message.channel, f)
								if result == "7":
									with open('/root/dismona/tyoudaikiti.png', 'rb') as f:
										await client.send_file(message.channel, f)
							elapsed_time = time.time() - start
							elapsed_time = str(elapsed_time)
							m = "貴方の今日の運勢は" + resultp + "です!\n0.000" + result2 + "Mona送りますね！"
							await client.send_message(message.channel, m)
							cursor.execute("INSERT INTO gived (id) VALUES (?)", (username,))
							m = "/tip <@" + username + "> 0.000" + result2 + " おみくじtipです！次挑戦できるのは日本時間で明日です！ . exectime: " + elapsed_time + " sec"
							await client.send_message(message.channel, m)
							connection.commit()
						else:
							def omikuji():
								kuji = ["0", "1", "2", "3", "2", "4"]
								result = random.choice(kuji)
								return result
							kuji = ["凶", "小吉", "中吉", "大吉", "超大吉"]
							result = omikuji()
							print("result")
							print(result)
							result = int(result)
							print("resulta")
							print(result)
							resultp = kuji[result]
							print("resultp")
							print(resultp)
							resultp = str(resultp)
							result = float(result) + float("3")
							result = int(result)
							result = str(result)
							kyou = "0"
							kyou = int(kyou)
							if result == "0":
								with open('/root/dismona/kyou.png', 'rb') as f:
									await client.send_file(message.channel, f)
							if result == "1":
								with open('/root/dismona/syoukiti.png', 'rb') as f:
									await client.send_file(message.channel, f)
							if result == "2":
								with open('/root/dismona/tyuukiti.png', 'rb') as f:
									await client.send_file(message.channel, f)
							if result == "3":
								with open('/root/dismona/daikiti.png', 'rb') as f:
									await client.send_file(message.channel, f)
							if result == "4":
								with open('/root/dismona/tyoudaikiti.png', 'rb') as f:
									await client.send_file(message.channel, f)
							elapsed_time = time.time() - start
							elapsed_time = str(elapsed_time)
							if result == kyou:
								m = "あなたの運勢…凶みたいだから、今日はそばにいてあげるんだからねっ！今日だけだからねっ"
							else:
								m = "ダーリン、あなたの今日の運勢は" + resultp + "らしいですわよ。!\n0.000" + result + "Mona送ってあげるわ。今日も気をつけてね、ダーリン。 . exectime: " + elapsed_time + " sec"
							await client.send_message(message.channel, m)
							cursor.execute("INSERT INTO gived (id) VALUES (?)", (username,))
							m = "/tip <@" + username + "> 0.000" + result + ""
							await client.send_message(message.channel, m)
							connection.commit()
					else:
						m = "スパム対策のためにTipしたことのないひとはおみくじを実行することができません。。だれかにtipしてもう一回実行おねがいします\nTo prevent spamming, user who never tiped before are not allowed to execute omikuji. please tip someone using /tip command."
						await client.send_message(message.channel, m)
				else:
					cursor.execute('SELECT banfromid FROM baned WHERE banedid = ' + username + '')
					banfromid = cursor.fetchall()
					banfromid = str(banfromid)
					m = "You are not allowed to /omikuzi! \n Detail:You are baned by <@" + banfromid + ">"
					await client.send_message(message.channel, m)
			else:
				m = "もう、<@" + message.author.id + "> 、何やってるの！！\n おみくじは1日一回ってあんなに言ったでしょ！ 明日まで禁止よ！\nそこに座ってなさい！"
				await client.send_message(message.channel, m)


		if message.content.startswith("/credit"):
			start = time.time()
			await client.add_reaction(message, '👌')
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
			embed = discord.Embed(title="Monage Discord Edition - Credit")
			embed.set_footer(text=" Created message at | " + currenttime + "")
			embed.add_field(name="raspi0124", value=" - 開発・制作")
			embed.add_field(name="はるまど", value=" - Gitlabの提供")
			embed.add_field(name="kakarichyo", value=" - クローズドアルファにおけるテスト")
			embed.add_field(name="和梨(ポテト)", value=" - クローズドアルファにおけるテスト")
			embed.add_field(name="MGQ", value=" - アドバイス、クローズドアルファにおけるテスト")
			embed.add_field(name="その他、Discordサーバー「MGQclub」のみなさん", value=" - テスト全般")
			embed.add_field(name="W.S Wsans", value=" - Discord.pyについてのアドバイス")
			embed.add_field(name="ぱい", value=" - Discord.pyについてのアドバイス")
			embed.add_field(name="lae", value=" - アドバイス、英語文法監修")
			embed.add_field(name="Limit", value=" - helpコマンドの見やすさの向上、リアクションtipのアイデア")
			embed.add_field(name="両親", value=" - 匿名にしておきます")
			embed.add_field(name="脇山P(wakip)", value=" - 大量の資金的な援助及びアドバイス")
			await client.send_message(message.channel, embed=embed)




		#MONAPARTY関連スタート
		if message.content.startswith('/mp info'):
			print("1")
			await client.add_reaction(message, '👌')
			headers = {
				'Content-Type': 'application/json; charset=UTF-8',
				'Accept': 'application/json, text/javascript',
			}
			data = '{ "jsonrpc": "2.0", "id": 0, "method": "get_running_info" }'
			print (data)
			response = requests.post('https://api.monaparty.me/api/counterparty', headers=headers, data=data, auth=('rpc', 'hello'))
			print(response)
			m = str(response)
			await client.send_message(message.channel, m)

		if message.content.startswith('/mp balance'):
			print("1")
			address = re.split('\W+', message.content)
			addresses = address[2]
			addresses = '"' + addresses + '"'

			headers = {
				'Content-Type': 'application/json; charset=UTF-8',
				'Accept': 'application/json, text/javascript',
			}
			data = '{ "jsonrpc": "2.0", "id": 0, "method": "get_normalized_balances" "addresses": ' + addresses +' }'
			response = requests.post('https://wallet.monaparty.me/_api', headers=headers, data=data, auth=('rpc', 'hello'))
			m = "here is " + addresses + " balance" + response + ""



			#MONAPARTY関連終わり



	if message.content.startswith("/"):
		#共用コマンド
		if message.content == "/cagreedtos":
			start = time.time()
				# データベース接続とカーソル生成
			username = message.author.id
			# エラー処理（例外処理）
			try:
				await client.add_reaction(message, '👌')
				fee = "0.01"
				cursor.execute("INSERT INTO agreetos (id) VALUES (?)", (username,))
				m = "利用規約への同意を確認しました。"
				await client.send_message(message.channel, m)
			except sqlite3.Error as e:
				print('sqlite3.Error occurred:', e.args[0])
				m = "DB error. DB might locked. Please try again later or contact @raspi0124."
				await client.send_message(message.channel, m)

			# 保存を実行（忘れると保存されないので注意）
			connection.commit()
		if message.content == "/agreetos":
			m = "ARE YOU REALLY SURE YOU AGREED TOS? READ THE TOS AGAIN!\n TOS can be found here: https://github.com/raspi0124/monage-term/blob/master/terms-ja.txt"
			await client.send_message(message.channel, m)
		if message.content == "/help":
			start = time.time()
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			embed = discord.Embed(title="Monage Discord Edition - Help")
			embed.set_footer(text=" Created message at | " + currenttime + "")
			embed.add_field(name="/help", value=" ヘルプを表示します")
			embed.add_field(name="/register", value="あなたの財布を新しく作成します <Create your address>")
			embed.add_field(name="/deposit - /list", value="あなたの所有しているアドレスを一覧表示します <List all address you have generated>")
			embed.add_field(name="/withdraw ``<amount to withdraw> <address to send>``", value="指定されたmonaを指定されたアドレスに送ります <Withdraw specified amount of Mona available to specified address>")
			embed.add_field(name="/tip ``<User to send Mona> <amount to tip> <Comment (optional)>``", value="指定されたmonaを指定されたユーザーに送ります <Tip specified amount of mona to specified user>")
			embed.add_field(name="/rain ``<number of people to tip> <total amount to tip>``", value=" 指定された金額のmonaをランダムに配ります。<Tip specified amount to random multiple people. You can choose the number of people to tip (Currently for admin only due to technical difficulties.)>")
			embed.add_field(name="/rera", value="rain受け取りに参加します。手数料は0.01monaです。 <Sign up to be a rain-reciever. fee is 0.01 mona currently, and might go up.>")
			embed.add_field(name="/omikuzi", value="おみくじ。おまけでmonaもらえます<Let see how fortunate you are! You can also get some mona!>")
			embed.add_field(name="/credit", value="クレジットを表示。 <Show credit>")
			embed.add_field(name="/agreetos", value="利用規約に同意する。。と見せかけてただのコマンドです。実際に同意するためのコマンドは利用規約に書いてあるのできちんと読んでください()")
			await client.send_message(message.channel, embed=embed)
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
		elif userid not in agreetos:
			m = "You need to agree tos in order to use Monage. Please type /help for more information.\n このコマンドを実行するには利用規約への同意が必要です。"
			await client.send_message(message.channel, m)

	cursor.close()
	connection.close()
client.run("NDA5MDkwMTE4OTU2MDg5MzQ0.DbzaFA.hPWfWE9cXQc5UjsUbo17diRoBOQ")
# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21
