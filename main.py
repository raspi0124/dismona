#Those code are licenced under gplv3, has no warrantly and you need to share the code in case you made a change.
#Copyright 2018 raspi0124.
import discord
import subprocess
import re
import time
import math
import random
import json
import string
import requests
import decimal
from decimal import (Decimal, ROUND_DOWN)
from decimal import Decimal
import hashlib
#import apim
#import sqlite3
import MySQLdb
from datetime import datetime
import mlibs
from discord.ext import commands
from ratelimiter import RateLimiter
from discord.ext.commands.cooldowns import BucketType
import sys
import os
import configparser

config = configparser.ConfigParser()
config.read('/root/dismona.conf')

section1 = 'development'
#status defines if its main server or backup server. Main server: 1, Sub server: 2 and 3
#status = config.get(section1, 'status')
discord_token = config.get(section1, 'discord_token')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')
#main_server_address = config.get(section1, 'main_server_address')
MONAGEID_SECRET = config.get(section1, 'MONAGEID_SECRET')
print("MAIN SERVICE IS NOW STARTING!")

print("Monage Discord Edition  Copyright (C) 2018  raspi0124\n \
	This program comes with ABSOLUTELY NO WARRANTY; for details, please read https://github.com/raspi0124/dismona/blob/master/LICENSE.\n \
	This is free software, and you are welcome to redistribute it\n \
	under certain conditions; read https://github.com/raspi0124/dismona/blob/master/LICENSE and if you have any question, email to raspi0124[@]gmail.com.")

client = discord.Client()
currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

print("0101")
# データベース接続とカーソル生成
connection = MySQLdb.connect(
	host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
cursor = connection.cursor()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print(currenttime)
	print('------')
	await client.change_presence(game=discord.Game(name='/help'))

@client.event
async def on_member_join(member):
	memberid = member.id
	membername = member.name
	serverid = member.server.id
	izaya_zatsudan = "415501395089686528"
	izaya_zatsudan = client.get_channel('415501395089686528')
	if serverid == "392277276470804480":
		m = "<@" + memberid + "> 何者だ！ 名を名乗れ！さもなくばこうだぞ！\n \
		(´・ω);y==ｰｰｰｰｰ  ・ ・   <:izaya:441956642125512734>    ・∵. ﾀｰﾝ"
		await client.send_message(izaya_zatsudan, m)
		m = "This service was requested by Daisuke and Kumatani and coded by raspi0124. If you have any question, please ask Daisuke or Kumatani, not raspi0124."
		message = await client.send_message(izaya_zatsudan, m)
		time.sleep(5)
		await client.delete_message(message)

@client.event
async def on_reaction_add(reaction, user):
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	cursor = connection.cursor()
	tipto = reaction.message.author.id
	tipby = user.id
	emoji = reaction.emoji.name
	tip0114114 = "monage0114114"
	tip039 = "monage039"
	if emoji == tip0114114:

		mlibs.unlockwallet()

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
				username = tipby
				tipamount = float(tipamount) / float(num2)
				tipamount = str(tipamount)
				mlibs.tip(tipby, tipto, tipamount)
				m = "<@" + tipby + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
				await client.send_message(reaction.message.channel, m)
			else:
				m = "<@" + tipby + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
				await client.send_message(reaction.message.channel, m)
		else:
			m = "<@"+ tipby + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
			await client.send_message(reaction.message.channel, m)

	if emoji == tip039:

		mlibs.unlockwallet()

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
				username = tipby
				tipamount = float(tipamount) / float(num2)
				tipamount = str(tipamount)
				cmd2 = "monacoin-cli move " + tipby + " " + tipto + " " + tipamount + ""
				mlibs.tip(tipby, tipto, tipamount)
				m = "<@" + tipby + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
				await client.send_message(reaction.message.channel, m)
			else:
				m = "<@" + tipby + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
				await client.send_message(reaction.message.channel, m)
		else:
			m = "<@"+ tipby + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
			await client.send_message(reaction.message.channel, m)


@client.event
@commands.cooldown(1, 5, BucketType.user)
async def on_message(message):
#	if status == "2":
#		main_server_status = is_page_available(main_server_address)
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	cursor.execute('SELECT * FROM ragreedtos')
	ragreedtos = cursor.fetchall()
	ragreedtos = mlibs.fixselect(ragreedtos)
	userid = message.author.id
	messagesql = str(message.content)
	useird = message.author.id
	rainnotify = "425766935825743882"
	rainnotify = client.get_channel('425766935825743882')
	timestamp = str(time.time())
	userid = message.author.id

	if message.content.startswith("/") and userid in ragreedtos:
		# 全件取得は cursor.fetchall()
		# 「/register」で始まるか調べる
		if message.content.startswith("/"):
			#各種ログを投入。
			towrite = "" + message.author.name + " said " + messagesql + ". userid: " + message.author.id + " channel id: " + message.channel.id + " currenttime: " + currenttime + "\n"
			file = open('/root/alllog2.txt', 'a')  #追加書き込みモードでオープン
			file.writelines(towrite)
			print(towrite)
			authorname = message.author.name
			authorid = message.author.id
			channelid = message.channel.id

			cursor.execute("INSERT INTO log (author, message, userid, channelid, currenttime) VALUES (%s, %s, %s, %s, %s)", (authorname, message.content, authorid, channelid, currenttime))
			#cursor.execute("INSERT INTO tmplog (author, message, userid, channelid, currenttime) VALUES (%s, %s, %s, %s, %s)", (authorname, message, authorid, channelid, currenttime))

			connection.commit()

		if message.content.startswith("/register"):
			#登録を処理。

			mlibs.unlockwallet()

			userid = message.author.id
			await client.add_reaction(message, '👌')
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
				# メッセージを書きます
				m = "<@" + message.author.id + "> さんのアカウントを作成しますね！"
				# メッセージが送られてきたチャンネルへメッセージを送ります
				await client.send_message(message.channel, m)
				#mlibsライブラリに投げる
				resultmore5 = mlibs.register(userid)
				m = "<@" + message.author.id + ">, successfully created an account for you! Your new address is " + resultmore5 + ", enjoy!"
				await client.send_message(message.channel, m)
				connection.commit()

		if message.content.startswith("/rera"):
			start = time.time()
				# データベース接続とカーソル生成
			username = message.author.id
			# エラー処理（例外処理）
			# INSERT
			#残高を取得
			balance = mlibs.libgetbalance(userid)
			if balance > "0.01":
				fee = "0.01"
				cursor.execute("INSERT INTO rainregistered (rainid) VALUES (%s)", (username,))
				cmd = "monacoin-cli move "  + message.author.id + " fee " + fee + ""
				ruta  =  subprocess.check_output( cmd.split(" ") )

				m = "Success."
				await client.send_message(message.channel, m)
				connection.commit()
			else:
				m = "Not enough balance to take fee. Please note that fee of 0.01mona will be charged for registering rain.(only once.)"
				await client.send_message(message.channel, m)

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
				address3 = mlibs.deposit(userid)
				#もしすでにアドレスが存在している場合
				if address3 != "":
					m = "<@" + message.author.id + ">, This is your deposit addresses: " + address3 + "\n(message created on " + currenttime + ")"
					await client.send_message(message.channel, m)
				#アドレスがまだ無い場合はここで作る
				else:
					address = mlibs.register(userid)
					m = "<@" + userid + ">, This is your deposit address: " + address + ""
					await client.send_message(message.channel, m)
		if message.content.startswith("/disagreetos"):
			#利用規約同意取り消し処理開始
			await client.add_reaction(message, '👌')
			m = "<@" + userid + "> Roger that. Now proceeding work.."
			await client.send_message(message.channel, m)
			m = "<@" + userid + "> Following thing will not happen after unless you agree tos again.\n \
			・ Loging message that starts with Monages prefix\n \
			Dont worry, your balance is still alive after this. Like as people who got tiped but not agreed tos yet.\n \
			If you want to start to use Monage again, just execute /agreetos again,read tos, than agree.\n \
			and .. Thanks for using Monage!"
			await client.send_message(message.channel, m)
			m = "<@" + userid + "> 以下のことは利用規約に再度同意しない限り起こることはありません。\n \
			・Monageのコマンド拡張子(prefix)から始まるメッセージの記録\n \
			心配しないでください、あなたの残高はtipされたが利用規約にまだ同意していないような人と同じように残ります。\n \
			もしMonageをまた使いたくなったら/agreetosを実行して利用規約を読んで同意するだけでまた使いはじめることができます。\n "
			await client.send_message(message.channel, m)
			m = "Now, removing you from agreetos database..(Should only take a sec)"
			await client.send_message(message.channel, m)
			#ここで利用規約同意データベースからuseridを削除
			cursor.execute("DELETE FROM ragreedtos WHERE id = %s", (userid,))
			cursor.execute("DELETE FROM agreetos WHERE id = %s", (userid,))
			connection.commit()
			m = "Finished removing you from agreetos database! and once again, Thanks for using Monage! and I hope to see you again!"
			await client.send_message(message.channel, m)
			m = "あなたを利用規約の同意データベースから削除しました。そして、Monageを使ってくださりありがとうございました。"
			await client.send_message(message.channel, m)
		if message.content.startswith("/list"):
			#addressは１つに統一したため/depositコマンドへの導線を。
			m = "This command is no longer available. please use /deposit command instead."
			await client.send_message(message.channel, m)
		if message.content.startswith("/withdraw"):
			#出金処理
			await client.add_reaction(message, '👌')
			#コマンドの処理を簡単にするために/withdrawを削除
			rmessage = message.content.replace('/withdraw', '')
			print(rmessage)
			pattern=r'([+-]?[0-9]+\.?[0-9]*)'
			print(re.findall(pattern,rmessage))
			#ここで出金額を取得するためにすべての数字を取得
			withdrawinfo = re.findall(pattern,rmessage)
			print(withdrawinfo[0])
			#出金金額は一番最初の数字でそれ以外はアドレスの文字列内の数字だと予想されるためここでamountを取り除き出金アドレスを取得
			amount = withdrawinfo[0]
			rmessage = rmessage.replace(amount, '')
			to = rmessage.replace(' ', '')
			withdraw_detail = mlibs.withdraw(userid, to, amount)
			print(withdraw_detail)
			withdraw_detail = str(withdraw_detail)
			#500は残高不足エラー
			if "500" in withdraw_detail:
				m = "<@" + userid + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
			else:
				m = "Withdraw successfull. TXID:" + withdraw_detail + ""
			await client.send_message(message.channel, m)
		if message.content.startswith("/givemylog"):
			#ログ取得
			m = "Sure, wait a min to get log. (Please note that we can only give you the log after 24 April since we were taking log with txt before that.)"
			await client.send_message(message.channel, m)
			#sqlを作成、直接実行ではなく一回収納しているのはコマンド実行するため。
			#コマンド実行する理由はSelectでcursorから取得しようとするとエラーが出るから
			sql = "SELECT * FROM log WHERE userid='{}'".format(userid)
			sql = '"' + sql + '"'
			command = "mysql -u{0} -p{1} dismona -e ".format(db_user, db_password)
			sqlcommand = command + sql
			cmd = sqlcommand
			rut  =  subprocess.check_output( cmd,  shell=True )
			cmd = "rm /root/tmp/tmplog.txt"
			rutaaa  =  subprocess.check_output( cmd,  shell=True )
			cmd = "touch /root/tmp/tmplog.txt"
			rutaaa  =  subprocess.check_output( cmd,  shell=True )
			rut = rut.decode()
			rut = str(rut)
			path_w = "/root/tmp/tmplog.txt"
			with open(path_w, mode='w') as f:
			    f.write(rut)

			with open(path_w) as f:
			    print(f.read())

			await client.send_file(message.channel, '/root/tmp/tmplog.txt')
			m = "Here are the log we took from you."
			await client.send_message(message.channel, m)

		if message.content.startswith("/givehislog"):
			if message.author.id == "326091178984603669":
				m = "Sure, wait a min to get log. (Please note that we can only give you the log after 24 April since we were taking log with txt before that.)"
				await client.send_message(message.channel, m)
				pattern=r'([+]?[0-9]+\.?[0-9]*)'
				messagecontent = message.content
				userid = re.findall(pattern, messagecontent)
				filenumber = "1"
				userid = userid[0]
				userid = str(userid)
				sql = "SELECT * FROM log WHERE userid='{}'".format(userid)
				sql = '"' + sql + '"'
				command = "mysql -u{0} -p{1} dismona -e ".format(db_user, db_password)
				sqlcommand = command + sql
				cmd = sqlcommand
				rut  =  subprocess.check_output( cmd,  shell=True )
				cmd = "rm /root/tmp/tmplog.txt"
				rutaaa  =  subprocess.check_output( cmd,  shell=True )
				cmd = "touch /root/tmp/tmplog.txt"
				rutaaa  =  subprocess.check_output( cmd,  shell=True )
				rut = rut.decode()
				rut = str(rut)
				path_w = "/root/tmp/tmplog.txt"
				with open(path_w, mode='w') as f:
				    f.write(rut)

				with open(path_w) as f:
				    print(f.read())

				await client.send_file(message.channel, '/root/tmp/tmplog.txt')
				m = "Here are the log we took from <" + userid + ">."
				await client.send_message(message.channel, m)
			else:
				print("a")

		if message.content.startswith("/rainall"):
			#rain実行
			start = time.time()

			mlibs.unlockwallet()

			#残高取得
			balancea = mlibs.libgetbalance(userid)
			await client.add_reaction(message, '👌')
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			#処理を簡単にするため/rainを削除
			message2 = message.content.replace('/rain ', '')
			pattern = r'([+-]?[0-9]+\.?[0-9]*)'
			raininfo = re.findall(pattern,message2)
			#rainする合計のmonaを指定
			print("--totalmona--")
			print(raininfo[0])
			totalmona = raininfo[0]
			print(totalmona)
			totalmona = float(totalmona)
			#エラー防止のために小数点第6位で四捨五入を実施。
			totalmona = round(totalmona,6)
			print(totalmona)
			totalmona = str(totalmona)
			cursor.execute('SELECT * FROM ragreedtos')
			# 全件取得は cursor.fetchall()
			rainall = cursor.fetchall()
			print(rainall)
			rainall = str(rainall)
			pattern=r'([+]?[0-9]+\.?[0-9]*)'
			rainall = re.findall(pattern,rainall)
			print(rainall)
			numofpeople = len(rainall)
			numofpeople = str(numofpeople)
			#permonaは1人当たりにrainされるmonaの量。totalmona/numofpeople = permona
			permona = float(totalmona) / float(numofpeople)
			totalmona = float(totalmona)
			totalmona = round(totalmona,6)
			totalmona = str(totalmona)
			permona = float(permona)
			if float(balancea) >= float(totalmona):
				if totalmona > "0.01":
					totalmona = str(totalmona)
					numofpeople = str(numofpeople)
					permona = str(permona)
					m = "you will rain in total of " + totalmona + "mona to " + numofpeople + " people.Amount of mona each user will get is " + permona + "mona."
					await client.send_message(message.channel, m)
					m = "Rain started by <@" + message.author.id + "> at #" + message.channel.name + ""
					await client.send_message(rainnotify, m)
					numofperople = int(numofpeople)

					for var in range(0, numofpeople):
						tosend = random.choice(rainall)
						print(tosend)
						print("--rondomfinish--")
						#tosend = int(tosend)
						#tosend = rainall[tosend]
						tosend = str(tosend)
						print("--startcommand--")
						#cmd = "monacoin-cli move " + message.author.id + " " + tosend + " " + sum + ""
						#rut  =  subprocess.check_output( cmd.split(" ") )
						#print(rut)
						mlibs.tip(userid, tosend, permona)
						m = "Raining" + permona + "mona to <@" + tosend + ">.."
						await client.send_message(rainnotify, m)
					numofpeople = str(numofpeople)
					m = "finished raining " + permona + "mona to " + numofpeople + "people! total amount was " + totalmona + "mona! Rained by <@" + message.author.id + ">"
					await client.send_message(message.channel, m)
					await client.send_message(rainnotify, m)
					print(rut)
				else:
					m = "Due to Server load, it is not allowed to make total amount of rain less then 0.01."
					await client.send_message(message.channel, m)
			else:
				m = "not enough fund.. double check amount to rain."
				await client.send_message(message.channel, m)

		if message.content.startswith("/rain"):
			#rain実行
			start = time.time()
			mlibs.unlockwallet()

			#残高取得
			balancea = mlibs.libgetbalance(userid)
			await client.add_reaction(message, '👌')
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			#処理を簡単にするため/rainを削除
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
			pattern=r'([+]?[0-9]+\.?[0-9]*)'
			rainall = re.findall(pattern,rainall)
			print(rainall)
			if balancea >= raininfo[1]:
				if raininfo[1] >= "0.01":
					m = "you will rain " + sum + "mona to " + raininfo[0] + " people."
					await client.send_message(message.channel, m)
					sum = str(sum)
					numbertosend = raininfo[0]
					numbertosend = int(numbertosend)
					m = "Rain started by <@" + message.author.id + "> at #" + message.channel.name + ""
					await client.send_message(rainnotify, m)
					for var in range(0, numbertosend):
						tosend = random.choice(rainall)
						print(tosend)
						print("--rondomfinish--")
						#tosend = int(tosend)
						#tosend = rainall[tosend]
						tosend = str(tosend)
						print("--startcommand--")
						mlibs.tip(userid, tosend, sum)
						m = "Raining" + sum + "mona to <@" + tosend + ">.."
						await client.send_message(rainnotify, m)
					m = "finished raining " + sum + "mona to " + raininfo[0] + "people! total amount was " + raininfo[1] + "mona! Rained by <@" + message.author.id + ">"
					await client.send_message(message.channel, m)
					m = "finished raining " + sum + "mona to " + raininfo[0] + "people! total amount was " + raininfo[1] + "mona! Rained by <@" + message.author.id + ">"
					await client.send_message(rainnotify, m)
					print(rut)
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
				message2 = message.content.replace('/ban', '')
				pattern = r'(\W+)'
				baninfo = re.findall(pattern,message2)
				print(baninfo[0])
				banto = baninfo[0]
				reason = ""
				reason = baninfo[1]

				if banto not in noban:
					cursor.execute("INSERT INTO baned (banedid) VALUES (%s)", (banto,))
					cursor.execute("INSERT INTO baned (banfromid) VALUES (%s)", (username,))
					cursor.execute("INSERT INTO baned (reason) VALUES (%s)", (reason,))
					m = "<@" + userid + "> ユーザー <@" + banto + "> をおみくじの使用及びshootizayaからBANしました。"
					await client.send_message(message.channel, m)
				else:
					m = "このユーザーをBANすることは禁止されています。"
					await client.send_message(message.channel, m)
			else:
				m = "You are not allowed to do that!"
				await client.send_message(message.channel, m)
		if message.content.startswith("/warn"):
			username = message.author.id
			banallow = ["326091178984603669", "294470458013908992"]
			noban = [""]
			if username in banallow:
				message2 = message.content
				message2 = message.content.replace('/warn', '')
				pattern = r'(\W+)'
				baninfo = re.findall(pattern,message2)
				print(baninfo[0])
				banto = baninfo[0]
				reason = ""
				reason = baninfo[1]

				if banto not in noban:

					m = "<@" + username + ">ユーザー <@" + banto + "> をDM上にて警告しました。"
					await client.send_message(message.channel, m)
				else:
					m = "このユーザーをBANすることは禁止されています。"
			else:
				m = "You are not allowed to do that!"
				await client.send_message(message.channel, m)

		if message.content.startswith("/tip"):
			start = time.time()
			mlibs.unlockwallet()

			message2 = message.content.replace('/tip', '')
			print (message2)
			pattern=r'([+-]?[0-9]+\.?[0-9]*)'
			print(re.findall(pattern,message2))
			tipinfo = re.findall(pattern,message2)
			print(tipinfo[0])
			print(tipinfo[1])
			tipto = tipinfo[0]
			tipamount = tipinfo[1]

			tip_detail = mlibs.tip(userid, tipto, tipamount)
			if "200" in tip_detail:
				m = "<@" + message.author.id + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ""
			if "e_10" in tip_detail:
				m = "<@" + message.author.id + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
			if "e_en" in tip_detail:
				m = "<@"+ message.author.id + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n "
			if "e_s" in tip_detail:
				m = "<@" + message.author.id + "> , You cannnot tip yourself."
			await client.send_message(message.channel, m)
			tipto = str(tipto)
			tipamount = float(tipamount)
			if tipto == "326091178984603669" and "200" in tip_detail:
				re3 = float("0.2")
				re1 = float("0.01")
				if tipamount >= re1:
					cursor.execute("DELETE FROM shooted WHERE id = %s", (userid,))
					cursor.execute("DELETE FROM shooted2 WHERE id = %s", (userid,))
					cursor.execute("DELETE FROM shooted3 WHERE id = %s", (userid,))
					m = "ありがとうございます！shootizayaの残弾をリセットしました！"
					await client.send_message(message.channel, m)
		if message.content.startswith("/admin info"):
			start = time.time()
			mlibs.unlockwallet()

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

			mlibs.unlockwallet()

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
			mlibs.unlockwallet()

			await client.add_reaction(message, '👌')
			for server in client.servers:
				for member in server.members.id:
					print (member)
					list_of_ids = [m.id  for m in server.members]
					print(list_of_ids)
		contributor = "" #fill this with SELCT for DB after.
		if message.content.startswith("/ad setimg "):
			if userid in contributor or userid == "326091178984603669":
				command = message.content.split(" ")
				url = command[2]
				if url.endswith(".png") or url.endswith(".jpg") or url.endswith(".gif") or url.endswith(".jpeg"):
					checkresult = mlibs.isurlexist(url)
					if checkresult == "0":
						m = "Your URL specified not seems to be an URL. Please check your url and try again."
						await client.send_message(message.channel, m)
					if checkresult == "0-1":
						m = "It looks like theres HTTP Error with server. Please check your URL and try again.(Just to remind you, Its usually impossible for us to access image on discord server, but we can check image on selfhosted web server, twitter or github.)"
						await client.send_message(message.channel, m)
					if checkresult == "0-2":
						m = "Not Found.Please check your URL and try again."
						await client.send_message(message.channel, m)
					if checkresult == "1":
						m = "OK, now adding this to DB.."
						await client.send_message(message.channel, m)

				else:
					m = "Your URL doesnt seems to be a image's url. Please specify image's url witch ends with image's extention"
					await client.send_message(message.channel, m)
			else:
				m = "You have no permission to execute this command!\n Please ask @raspi0124 for permission."
				await client.send_message(message.channel, m)
		if message.content.startswith("/ad settxt"):
			if userid in contributor or userid == "326091178984603669":
				command = message.content.split(" ")
				text = command[2]
				if text == "":
					m = "TEXT NOT SPECIFIED ERROR"
					await client.send_message(message.channel, m)
				else:
					m = "Adding your text ad to DB.."
					await client.send_message(message.channel, m)
		if message.content.startswith('/adminregister'):
			mlibs.unlockwallet()
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
		if message.content == "/kill main":
			m = "OK, killing main process.."
			await client.send_message(message.channel, m)
			sys.exit()
		if message.content.startswith('/adminbalance'):
			mlibs.unlockwallet()

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
		if message.content == "/makemenew":
			m = "Sure, Lets me make your account newer!"
			await client.send_message(message.channel, m)
			#accountlist