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
from decimal import Decimal
#import apim
#import sqlite3
import MySQLdb
from datetime import datetime
import mlibs
from discord.ext import commands
from ratelimiter import RateLimiter
from discord.ext.commands.cooldowns import BucketType
print("MAIN SERVICE IS NOW STARTING!")

def limited(until):
    duration = int(round(until - time.time()))
    print('Rate limited, sleeping for {:d} seconds'.format(duration))

rate_limiter = RateLimiter(max_calls=2, period=1, callback=limited)

def round_down5(value):
	value = Decimal(value).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)
	return value

client = discord.Client()
currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

print("0101")
# データベース接続とカーソル生成
# 接続情報はダミーです。お手元の環境にあわせてください。
connection = MySQLdb.connect(
   host='localhost', user='root', passwd='laksjd', db='dismona', charset='utf8')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS dismona.id (id VARCHAR(20), address VARCHAR(50));")


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
	connection = MySQLdb.connect(db='dismona',user='root',passwd='laksjd',charset='utf8mb4')
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
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
				username = tipby
				tipamount = float(tipamount) / float(num2)
				tipamount = str(tipamount)
				mlibs.tip(tipby, to, tipamount)
				m = "<@" + tipby + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
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
				username = tipby
				tipamount = float(tipamount) / float(num2)
				tipamount = str(tipamount)
				cmd2 = "monacoin-cli move " + tipby + " " + tipto + " " + tipamount + ""
				mlibs.tip(tipby, to, tipamount)
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
	connection = MySQLdb.connect(db='dismona',user='root',passwd='laksjd',charset='utf8mb4')
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	cursor.execute('SELECT * FROM agreetos')
	agreetos = cursor.fetchall()
	agreetos = mlibs.fixselect(agreetos)
	#pattern = r'([0-9]+\.%s[0-9]*)'
	#agreetos = re.findall(pattern,agreetos)
	#print(agreetos)
	userid = message.author.id
	messagesql = str(message.content)
	useird = message.author.id
	rainnotify = "425766935825743882"
	rainnotify = client.get_channel('425766935825743882')
	timestamp = str(time.time())
	userid = message.author.id

	if message.content.startswith("/") and message.content != "/agreetos" and message.content != "/cagreedtos" and message.content != "/help" and userid in agreetos or message.author.id == "409090118956089344":
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
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
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
				print(ruta)
				m = "Success. exectime: " + elapsed_time + " sec"
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
			sql = "SELECT * FROM log WHERE userid='" + userid + "'"
			sql = '"' + sql + '"'
			command = "mysql -uroot -plaksjd dismona -e "
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
				sql = "SELECT * FROM log WHERE userid='" + userid + "'"
				sql = '"' + sql + '"'
				command = "mysql -uroot -plaksjd dismona -e "
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
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
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
			cursor.execute('SELECT * FROM agreetos')
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
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
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
					if sum > "0.0001":
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
						m = "負荷軽減のため1人当たりのrainが0.0001mona以下になるrainは制限しています。"
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
			cmda = "monacoin-cli walletpassphrase 0124 10"
			ruta  =  subprocess.check_output( cmda.split(" ") )
			print(ruta)
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
					cursor.execute("DELETE FROM shooted WHERE id = " + userid + "")
					cursor.execute("DELETE FROM shooted2 WHERE id = " + userid + "")
					cursor.execute("DELETE FROM shooted3 WHERE id = " + userid + "")
					m = "ありがとうございます！shootizayaの残弾をリセットしました！"
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
		if message.content == "/makemenew":
			m = "Sure, Lets me make your account newer!"
			await client.send_message(message.channel, m)
			cursor.execute("INSERT INTO accounts (discordid, monageid, timestamp) VALUES (userid,)")
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
		if message.content.startswith("/rmshootizaya"):
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			start = time.time()
			if message.author.id == "326091178984603669":
				cmd = 'sh dismona-rmshoot.sh'
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
			loved = list(loved)
			loved = str(loved)
			loved = loved.replace('(', '')
			loved = loved.replace(')', '')
			loved = loved.replace("b'", '')
			loved = loved.replace("'", '')
			loved = loved.replace(",,", ',')
			loved = loved.replace("[", '')
			loved = loved.replace("]", '')
			loved = loved.split(',')
			loved = str(loved)
			cmd = "monacoin-cli getbalance " + message.author.id + ""
			rut  =  subprocess.check_output( cmd.split(" ") )
			balance = rut.decode()
			print(balance)
			balance = balance.replace("\n", '')
			balance = balance.replace("\\n", '')
			balance = float(balance)
			if message.author.id == "406829226751295488":
				m = "友達にもなりたくないです。二度と話しかけないでください"
				await client.send_message(message.channel, m)
			else:
				if username not in loved:
					minbal = "1"
					minbal = float(minbal)

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
							cursor.execute("INSERT INTO loved (id) VALUES (%s)", (username,))
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
			await client.delete_message(message)
		if message.content.startswith("/checkbalance"):
			cmdlib = "monacoin-cli getbalance '*' 1"
			rutlib  =  subprocess.check_output( cmdlib.split(" ") )
			balanceall = rutlib.decode()
			balanceall = float(balanceall)
			cmdlib = "monacoin-cli getbalance"
			rutlib  =  subprocess.check_output( cmdlib.split(" ") )
			balancelib = rutlib.decode()
			balancelib = float(balancelib)
			balancelib = str(balancelib)
			balanceall = str(balanceall)
			m = "Wallet Balance:" + balancelib + " DB balance:" + balanceall + ""
			await client.send_message(message.channel, m)
			result = float(balancelib) - float(balanceall)
			result = str(result)
			m = "Difference between DB balance and Wallet balance are " + result + " mona"
			await client.send_message(message.channel, m)
		if message.content.startswith("/marryhim"):
			if message.author.id == "326091178984603669":
				username = message.author.id
				cursor.execute('SELECT * FROM loved')
				loved = cursor.fetchall()
				print(loved)
				loved = str(loved)
				pattern = r'([0-9]+\.%s[0-9]*)'
				loved = re.findall(pattern,loved)
				message1 = message.content
				tolove = re.findall(pattern,message1)
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
							cursor.execute("INSERT INTO loved (id) VALUES (%s)", (tolove,))
							connection.commit()
						await client.send_message(message.channel, m)
					else:
						def loved():
							kuji = ["0"]
							result = random.choice(kuji)
							return result
						messeages = ["すでにあの方と結婚していますが何か%s"]
						result = loved()
						result = int(result)
						m = messeages[result]
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
			embed.add_field(name="Ming", value=" - おみくじイラストの作成")
			embed.add_field(name="両親", value=" - 匿名にしておきます")
			embed.add_field(name="脇山P(wakip)", value=" - 大量の資金的な援助及びアドバイス")
			await client.send_message(message.channel, embed=embed)




		#MONAPARTY関連スタート

		if message.content.startswith('/mp balance'):
			print("1")
			addresses = mlibs.deposit(message.author.id)
			addresses = '"' + addresses + '"'
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
			response = requests.post('https://wallet.monaparty.me/_api', headers=headers, data=data, auth=('rpc', 'hello'))
			print(response)
			print(response.text)

			responsejson = response.json()
			responseresult = responsejson['result']

			print(responseresult)
			print("")
			numresult = int(len(responseresult))
			for num in range(numresult):
				print(num)
				print(json.dumps(responseresult[num]))
				m = json.dumps(responseresult[num])
				json_dict = json.loads(m)
				assetname = str(json_dict['asset'])
				assetamount = str(json_dict['normalized_quantity'])
				m = "" + assetname + " : " + assetamount + " " + assetname + ""
				await client.send_message(message.channel, m)
			responseresult = str(responseresult)

		if message.content.startswith("/mp deposit"):
			await client.add_reaction(message, '👌')
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
				# メッセージを書きます
				m = "<@" + message.author.id + "> アドレスを確認中..."
				# メッセージが送られてきたチャンネルへメッセージを送ります
				await client.send_message(message.channel, m)
				address3 = mlibs.deposit(userid)
				m = "<@" + message.author.id + ">, This is your monaparty deposit addresses: " + address3 + "\n(message created on " + currenttime + ")"
				await client.send_message(message.channel, m)

		if message.content.startswith("/mp tip"):
			if message.author.id == "326091178984603669":
				await client.add_reaction(message, '👌')
				print("start")
				beforebal = mlibs.libgetbalance(userid)
				message2 = message.content.replace('/mp tip', '')
				print (message2)
				pattern = r'\w+'
				print(re.findall(pattern,message2))
				tipinfo = re.findall(pattern,message2)
				print(tipinfo[0])
				print(tipinfo[1])
				tipto = tipinfo[0]
				tipamount = tipinfo[1]
				tiptoken = tipinfo[2]
				print("")
				print(tipto)
				print(tipamount)
				print(tiptoken)
				print("")
				pattern=r'([+-]?[0-9]+\.?[0-9]*)'
				tipto = re.findall(pattern,tipto)
				tipto = str(tipto[0])
				addresses = mlibs.deposit(userid)
				address = mlibs.deposit(userid)
				print(address)
				print(addresses)
				addresses = '"' + addresses + '"'
				tiptoaddress = mlibs.deposit(tipto)
				tiptoaddress = '"' + tiptoaddress + '"'
				tiptoken = '"' + tiptoken + '"'
				#pubkey = mlibs.getpubkey(address)
				#pubkey = '"' + pubkey + '"'
				#APIにアクセスし該当TXIDをもらってくる
				fee = "2000"

				headers = {
					'Content-Type': 'application/json; charset=UTF-8',
					'Accept': 'application/json, text/javascript',
				}

				data = '{"jsonrpc":"2.0", "id":0, "method":"get_asset_info", "params":{"assets":[' + tiptoken + ']} }'

				asset_info = requests.post('http://153.126.176.183:4000/api/ ', headers=headers, data=data, auth=('rpc', 'rpc'))
				assetinfo_json = asset_info.json()
				print(assetinfo_json)
				print(assetinfo_json['result'])
				rut = assetinfo_json['result']
				rut = str(rut)
				rut = rut.replace('\\n', '')
				rut = rut.replace("b'", '')
				rut = rut.replace("'", '"')
				rut = rut.replace("True", '"True"')
				rut = rut.replace("False", '"False"')
				ut = rut.replace("None", '"None"')
				print(rut)
				json_dict = json.loads(rut)
				isdivisible = str(json_dict['divisible'])
				print(isdivisible)

				print("---Assetinfo compleate---")
				data = '{\n \
	  			"method": "create_send",\n \
	  			"params": {"source": ' + addresses + ', "destination": ' + tiptoaddress + ', "asset": ' + tiptoken + ', "quantity": ' + tipamount + ', "fee": ' + fee + ', "allow_unconfirmed_inputs": true, "use_enhanced_send": false },\n \
	  			"jsonrpc": "2.0",\n \
	  			"id": 1\n \
				}'


				print(data)
				response = requests.post('http://153.126.176.183:4000/api/', headers=headers, data=data, auth=('rpc', 'rpc'))
				print(response)
				print(response.text)
				print("---create_send request compleate---")
				print("")
				responsejson = response.json()
				rawtransaction = responsejson['result']
				print(rawtransaction)
				rawtransaction = str(rawtransaction)
				print("")
				mlibs.unlockwallet(30)
				cmd = "monacoin-cli signrawtransaction " + rawtransaction + ""
				rut = subprocess.check_output( cmd.split(" ") )
				rut = str(rut)
				rut = rut.replace('\\n', '')
				rut = rut.replace("b'", '')
				rut = rut.replace("'", '')
				if "true" in rut:
					rut = rut.replace("true", '"true"')
				if "false" in rut:
					rut = rut.replace("false", '"false"')
				print(rut)
				#m = json.dumps(rut)
				m = rut
				json_dict = json.loads(m)
				hex = str(json_dict['hex'])
				cmd = "monacoin-cli sendrawtransaction " + hex + ""
				txid = subprocess.check_output( cmd.split(" ") )
				tipamount = str(tipamount)
				tiptoken = str(tiptoken)
				userid = str(userid)
				tipto = str(tipto)
				txid = str(txid)
				m = "Successfully sent " + tipamount + " " + tiptoken + " from <@" + userid + "> to <@" + tipto +"> !\n TXID: " + txid + ""
				await client.send_message(message.channel, m)
			else:
				m = "Sorry, But for security reason, executing /mp tip command are only allowed for developer."
				await client.send_message(message.channel, m)

#MONAPARTY関連終わり



	if message.content.startswith("/"):
		#共用コマンド
		if message.content == "/cagreedtos":
			start = time.time()
				# データベース接続とカーソル生成
			username = message.author.id
			# エラー処理（例外処理）
			await client.add_reaction(message, '👌')
			fee = "0.01"
			cursor.execute("INSERT INTO agreetos (id) VALUES (%s)", (username,))
			m = "利用規約への同意を確認しました。"
			await client.send_message(message.channel, m)
			cursor.execute('SELECT * FROM agreetos')
			agreetos = cursor.fetchall()
			agreetos = str(agreetos)
			print(agreetos)


			# 保存を実行（忘れると保存されないので注意）
			connection.commit()
		if message.content == "/agreetos":
			m = "利用規約はきちんと読みましたか？もう一度確認してみましょう。→　https://github.com/raspi0124/monage-term/blob/master/terms-ja.txt\n Please read tos and try again. Tos can be found at → https://github.com/raspi0124/monage-term/blob/master/terms-en.txt"
			await client.send_message(message.channel, m)
		if message.content == "/help":
			start = time.time()
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			embed = discord.Embed(title="Monage Discord Edition - Help")
			embed.set_footer(text=" Created message at | " + currenttime + "")
			embed.add_field(name="/help", value=" ヘルプを表示します")
			embed.add_field(name="/register", value="あなたの財布を新しく作成します <Create your address>")
			embed.add_field(name="/deposit", value="あなたの所有しているアドレスを一覧表示します <List all address you have generated>")
			embed.add_field(name="/withdraw ``<amount to withdraw (出金量)> <address to send(アドレス)>``", value="指定されたmonaを指定されたアドレスに送ります <Withdraw specified amount of Mona available to specified address>")
			embed.add_field(name="/tip ``<User to send Mona(送り先ユーザー)> <amount to tip(tip量)> <Comment (optional)>``", value="指定されたmonaを指定されたユーザーに送ります <Tip specified amount of mona to specified user>")
			embed.add_field(name="/rain ``<number of people to tip> <total amount to tip>``", value=" 指定された金額のmonaをランダムに配ります。<Tip specified amount to random multiple people. You can choose the number of people to tip (Currently for admin only due to technical difficulties.)>")
			embed.add_field(name="/rera", value="rain受け取りに参加します。手数料は0.01monaです。 <Sign up to be a rain-reciever. fee is 0.01 mona currently, and might go up.>")
			embed.add_field(name="/omikuzi", value="おみくじ。おまけでmonaもらえます<Let see how fortunate you are! You can also get some mona!>")
			embed.add_field(name="/mp deposit", value="Monapartyの入金アドレスを表示します。(現在テスト中なのでGOXしたりしても泣かないトークンのみ送ってください)")
			embed.add_field(name="/mp balance", value="Monapartyトークンの残高を表示します。")
			embed.add_field(name="/credit", value="クレジットを表示。 <Show credit>")
			embed.add_field(name="/givemylog", value="あなたのログをエクスポート。そのままチャンネルに吐き出すのでDMでの実行を強くおすすめします。<Export log. Executing this command in DM is highly recommended.>")
			embed.add_field(name="/agreetos", value="利用規約に同意する。。と見せかけてただのコマンドです。実際に同意するためのコマンドは利用規約に書いてあるのできちんと読んでください()")
			embed.add_field(name="/disagreetos", value="利用規約への同意を取りやめるコマンドです。なお、残高は残り続けますし、利用規約に同意しなおすことでまた使うことができます。 <Disagree the tos. Balance will still remain, and you may use it at anytime by agreeing the tos again.>")
			await client.send_message(message.channel, embed=embed)
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
		elif userid not in agreetos and message.author.id != "409090118956089344":
			m = "You need to agree tos in order to use Monage. Please type /help for more information.\n このコマンドを実行するには利用規約への同意が必要です。→　https://github.com/raspi0124/monage-term/blob/master/terms-ja.txt\n Please read tos and try again. Tos can be found at → https://github.com/raspi0124/monage-term/blob/master/terms-en.txt"
			await client.send_message(message.channel, m)

	connection.commit()
	connection.close()
client.run("NDA5MDkwMTE4OTU2MDg5MzQ0.Ddop9Q.K1wjAC3ZztBltTDp75ijN0baj-I")
# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21
