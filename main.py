#Those code are licenced under gplv3, has no warrantly and you need to share the code in case you made a change.
#Copyright 2018 raspi0124.
import discord
import subprocess
import re
import time
import random
import json
import requests
import hashlib
#import apim
#import sqlite3
import MySQLdb
from datetime import datetime
import mlibs
import maclib
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sys
import configparser
import rollbar



config = configparser.ConfigParser()
config.read('dismona.conf')

section1 = 'complylaw'
#status defines if its main server or backup server. Main server: 1, Sub server: 2 and 3
#status = config.get(section1, 'status')
discord_token = config.get(section1, 'discord_token')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')
rollbar_key = config.get(section1, 'rollbar_key')
#main_server_address = config.get(section1, 'main_server_address')
MONAGEID_SECRET = config.get(section1, 'MONAGEID_SECRET')
print("<COMPLY-LAW VERSION>MAIN SERVICE IS NOW STARTING!")

print("Monage Discord Edition  Copyright (C) 2018  raspi0124\n \
	This program comes with ABSOLUTELY NO WARRANTY; for details, please read https://github.com/raspi0124/dismona/blob/master/LICENSE.\n \
	This is free software, and you are welcome to redistribute it\n \
	under certain conditions; read https://github.com/raspi0124/dismona/blob/master/LICENSE and if you have any question, email to raspi0124[@]gmail.com.")

client = discord.Client()
currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

rollbar.init(rollbar_key)
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


@client.event #noqa
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
	userid = str(message.author.id)
	messagesql = str(message.content)
	rainnotify = "425766935825743882"
	rainnotify = client.get_channel('425766935825743882')
	print("userid", type(userid))
	print("ragreedtos", type(ragreedtos))
	commands = ["register","rera","balance","price","deposit","disagreetos",\
	"list","withdraw","givemylog","givehislog","rainall","rain","ban","warn",\
	"tip","admin info","adminc","members","ad","adminregister","kill",\
	"adminbalance","makemenew","image","hello","rmomikuzi","rmshootizaya",\
	"love","restart","marryhim","credit","mp","cagreedtos","ragreedtos",\
	"agreetos","help","shootizaya","omikuzi","omikuji", "show", "oldbalance"]


	if str(userid) in ragreedtos:
		# 全件取得は cursor.fetchall()
		# 「/nregister」で始まるか調べる
		if message.content.startswith("/"):
			#各種ログを投入。
			towrite = "" + message.author.name + " said " + messagesql + ". userid: " + str(userid) + " channel id: " + str(message.channel.id) + " currenttime: " + str(currenttime) + "\n"
			file = open('/root/dismona_devlog.txt', 'a')  #追加書き込みモードでオープン
			file.writelines(towrite)
			print(towrite)
			authorname = message.author.name
			authorid = userid
			channelid = message.channel.id
			logmessage = "[LAWCOMPLY]" + message.content
			cursor.execute("INSERT INTO log (author, message, userid, channelid, currenttime) VALUES (%s, %s, %s, %s, %s)", (authorname, logmessage, authorid, channelid, currenttime))
			#cursor.execute("INSERT INTO tmplog (author, message, userid, channelid, currenttime) VALUES (%s, %s, %s, %s, %s)", (authorname, message, authorid, channelid, currenttime))
			connection.commit()

		if message.content.startswith("/nregist"):
			m = "Welcome to brand new register command here! Please access https://gallant-jackson-e57582.netlify.com/address.html to get token."
			splitedm = message.content.split(" ")
			if splitedm[1] != "" or splitedm [1] != None:
				hashedaddress = splitedm[1]

		if message.content.startswith("/nregistmyaddress"):
			m = "NOTICE: THIS COMMAND IS ONLY AVAILABLE TO THE USERS WHO ARE NOT ABLE TO USE MPurse and decided to use own wallet. We highly recommend you to use /nregist command instead. Continue? Type /nregister."
			await client.send_message(message.channel, m)
			m = "注意: このコマンドはあくまでMPurseが全く使えない方のために用意したコマンドです。運営としましてはもしMPurseが使えるようでしたら /nregist コマンドを使用されることを強くお勧めしております。もし続けたい場合は /nregister と打ってください。"
			await client.send_message(message.channel, m)

		if message.content.startswith("/nregister"):
			splitedm = message.content.split(" ")
			if splitedm[1] != "" or splitedm [1] != None:
				address = splitedm[1]
				if maclib.reguseraddress(userid, address):
					m = "アドレス: " + address + " を正常に登録しました。/deposit コマンドで確認できます。"
					await client.send_message(message.channel, m)
					m = "Address " + address + " has been successfully registered. You should now be able to confirm it by executing /deposit command."
					await client.send_message(message.channel, m)
				else:
					m = "False response returned. Maybe wrong type of address or already registered?\n If you have already registered, please use /updatemyaddress command instead to update your address."
					await client.send_message(message.channel, m)
					m = "無効なレスポンスが返ってきました。アドレスが間違っているかすでに登録済みではないですか? /updatemyaddress を代わりに使ってみるといいかもしれません。"

		if message.content.startswith("/updatemyaddress"):
			splitedm = message.content.split(" ")
			address = splitedm[1]
			if maclib.updateuseraddress(userid, address):
				m = "Successfully updated your address to " + address + "."
				await client.send_message(message.channel, m)
			else:
				m = "False response returned. Maybe wrong type of address or not yet registered? Remember, you need to execute /nregister command in order to start using Monage."
				await client.send_message(message.channel, m)
		if message.content.startswith("/adminmonageid"):
			if userid == "326091178984603669":
				splitedm = message.content.split(" ")
				userid = splitedm[1]
				res = maclib.getmonageid(userid)
				m = res
				await client.send_message(message.channel, m)
		if message.content.startswith("/adminregistaddress"):
			if userid == "326091178984603669":
				splitedm = message.content.split(" ")
				if splitedm[1] != "" or splitedm [1] != None:
					reguserid = splitedm[1]
					regaddress = splitedm[2]
					if maclib.reguseraddress(reguserid, regaddress):
						m = "アドレス: " + regaddress + " を " + reguserid +" に正常に登録しました。/deposit コマンドで確認できます。"
						await client.send_message(message.channel, m)
						m = "Address " + regaddress + " has been successfully registered. You should now be able to confirm it by executing /deposit command."
						await client.send_message(message.channel, m)
					else:
						m = "False response returned. Maybe wrong type of address or already registered?"
						await client.send_message(message.channel, m)

		if message.content.startswith("/checkaddress"):
			splitedm = message.content.split(" ")
			pattern=r'([+-]?[0-9]+\.?[0-9]*)'
			print(re.findall(pattern, splitedm[1]))
			tocheck = re.findall(pattern, splitedm[1])
			res = maclib.getusersaddress(tocheck[0])
			m = res
			await client.send_message(message.channel, m)

		if message.content.startswith("/mymonageid"):
			result = maclib.getmonageid(userid)
			if "ERRROR" in result:
				m = "まずアドレスを登録してください!"
			else:
				m = "あなたのMonage IDは" + result + "です!"
			await client.send_message(message.channel, m)

		if message.content.startswith("/balance"):
			m = "<@" + userid + "> さんの残高チェック中.."
		# メッセージが送られてきたチャンネルへメッセージを送ります
			await client.send_message(message.channel, m)
			balance = str(mlibs.libgetbalance(maclib.getusersaddress(userid)))
			jpybalance = str(mlibs.libgetjpybalance(userid))
			m = "<@" + userid + ">, you currently have  " + balance + " mona!(JPY " + jpybalance +  ")\n(message created on " + currenttime + ")"
			print ("---6---")
			await client.send_message(message.channel, m)
		
		if message.content.startswith("/oldbalance"):
			m = "<@" + userid + "> さんの旧Monage上での残高チェック中.."
		# メッセージが送られてきたチャンネルへメッセージを送ります
			await client.send_message(message.channel, m)
			balance = str(mlibs.libgetbalance(mlibs.getoldbalance(userid)))
			m = "<@" + userid + ">さんの旧Monage上での残高は " + balance + " monaです! 引き出し期限は10月31日までとなっているので引き出しはお早めにどうぞ!\n(message created on " + currenttime + ")"
			tm = "注意: 現在自動引き出しは未実装のため引き出したい際はraspi0124までDMをお願いします。"
			await client.send_message(message.channel, m)
			await client.send_message(message.channel, tm)

		if message.content.startswith("/price"):
			cp = mlibs.getcurrentprice()
			m ="いまmonaは" + cp + "円です！"
			await client.send_message(message.channel, m)

		if message.content.startswith("/deposit"):
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
				address3 = maclib.getusersaddress(userid)
				#もしすでにアドレスが存在している場合
				if address3 != "NF":
					m = "<@" + userid + ">, This is your registered deposit addresses: " + address3 + "\n(message created on " + currenttime + ")"
					await client.send_message(message.channel, m)
				#アドレスがまだ無い場合はここで作る
				else:
					m = "<@" + userid + ">, no address registered yet.."
					await client.send_message(message.channel, m)

		if message.content.startswith("/show othersaddress"):
			splitedm = message.content.split(" ")
			targetuserid = splitedm[2]
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
				address3 = maclib.getusersaddress(targetuserid)
				#もしすでにアドレスが存在している場合
				if address3 != "":
					m = "<@" + userid + ">, This is his/her registered deposit addresses: " + address3 + "\n(message created on " + currenttime + ")"
					await client.send_message(message.channel, m)
				#アドレスがまだ無い場合はここで作る
				else:
					m = "<@" + userid + ">, no address registered for specified user yet.."
					await client.send_message(message.channel, m)

		if message.content.startswith("/disagreetos"):
			#利用規約同意取り消し処理開始
			m = "<@" + userid + "> Roger that. Now proceeding work.."
			await client.send_message(message.channel, m)
			m = "<@" + userid + "> Following thing will not happen after unless you agree tos again.\n \
			・ Loging message that starts with Monages prefix\n \
			Dont worry, your balance will yet remain like as people who got tiped but not agreed tos yet.\n \
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
			m = "I'm sorry, but this command no longer work with us. He was literaly forced to quit due to certain restriction being enabled by Japanese Government.. Instead, please do withdraw from the Monage Bridge platform"
			await client.send_message(message.channel, m)
			m = "新システムへの移行によって資金の保存先がクライアントのデバイスになったためWithdrawコマンドを廃止しました。もしMonage Discord Editionに使っているアドレスから出金されたい場合はMonage Bridgeよりお願いします。"
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
			subprocess.check_output( cmd,  shell=True )
			cmd = "touch /root/tmp/tmplog.txt"
			subprocess.check_output( cmd,  shell=True )
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
			if userid == "326091178984603669":
				m = "Sure, wait a min to get log. (Please note that we can only give you the log after 24 April since we were taking log with txt before that.)"
				await client.send_message(message.channel, m)
				pattern=r'([+]?[0-9]+\.?[0-9]*)'
				messagecontent = message.content
				userid = re.findall(pattern, messagecontent)
				userid = userid[0]
				userid = str(userid)
				sql = "SELECT * FROM log WHERE userid='{}'".format(userid)
				sql = '"' + sql + '"'
				command = "mysql -u{0} -p{1} dismona -e ".format(db_user, db_password)
				sqlcommand = command + sql
				cmd = sqlcommand
				rut  =  subprocess.check_output( cmd,  shell=True )
				cmd = "rm /root/tmp/tmplog.txt"
				subprocess.check_output( cmd,  shell=True )
				cmd = "touch /root/tmp/tmplog.txt"
				subprocess.check_output( cmd,  shell=True )
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

		if message.content.startswith("/warn"):
			username = userid
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
			message2 = message.content.replace('/tip', '')
			print (message2)
			pattern=r'([+-]?[0-9]+\.?[0-9]*)'
			print(re.findall(pattern,message2))
			tipinfo = re.findall(pattern,message2)
			print("TIPINFO", tipinfo)
			print(tipinfo[0])
			print(tipinfo[1])
			tipto = tipinfo[0]
			tipamount = tipinfo[1]
			tip_detail = mlibs.tip(str(userid), str(tipto), tipamount)
			m = "↓のリンクをクリックして送金してください!\n" + tip_detail
			await client.send_message(message.channel, m)

		if message.content.startswith("/admin info"):
			start = time.time()
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			m = "Verfifying.. wait a monemt"
			await client.send_message(message.channel, m)
			if userid == "326091178984603669":
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

		if message.content.startswith('/members'):


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
			m = "This command is no longer available. Use /adminregistaddress instead."
		if message.content == "/kill main":
			m = "OK, killing main process.."
			await client.send_message(message.channel, m)
			sys.exit()
		if message.content.startswith('/adminbalance'):
			if userid == "326091178984603669":
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
			with open('../image.png', 'rb') as f:
				await client.send_file(message.channel, f)

		if message.content.startswith("/hello"):
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			start = time.time()
			m = "こんにちは! <@" + userid + "> さん！"
			await client.send_message(message.channel, m)
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
			m = "elapsed time:" + elapsed_time + "sec"
			await client.send_message(message.channel, m)

		if message.content.startswith("/rmomikuzi"):
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			start = time.time()
			if userid == "326091178984603669":
				cmd = "sh dismona-rm.sh"
				subprocess.check_output( cmd.split(" ") )
				m = "True"
				await client.send_message(message.channel, m)
				elapsed_time = time.time() - start
				elapsed_time = str(elapsed_time)
				m = "elapsed time:" + elapsed_time + "sec"
				await client.send_message(message.channel, m)


		if message.content.startswith("/love"):
			start = time.time()
			username = userid
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
			cmd = "monacoin-cli getbalance " + userid + ""
			rut  =  subprocess.check_output( cmd.split(" ") )
			balance = rut.decode()
			print(balance)
			balance = balance.replace("\n", '')
			balance = balance.replace("\\n", '')
			balance = float(balance)
			if userid == "406829226751295488":
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
						cursor.execute("DELETE FROM loved WHERE id = %s", (userid,))
						connection.commit()
					await client.delete_message(message)
			await client.delete_message(message)

		if message.content.startswith("/restart"):
			if userid == "326091178984603669":
				command = message.content.split(" ")
				module = command[1]
				if module == "main":
					m = "OK, now proceeding to restart main module.. This process might take a while."
					await client.send_message(message.channel, m)
					cmd = "refresh"
					subprocess.Popen(cmd)
					m = "Launched new process. Killing current Main Module's process in 3 sec."
					await client.send_message(message.channel, m)
					time.sleep(3)
					exit()
				if module == "all":
					m = "OK, proceeding restart for all module.\n Starting Backup Module.."
					await client.send_message(message.channel, m)
					time.sleep(3)
					exit()
					cmd = "startbackup"
					subprocess.Popen(cmd)

			if userid == "326091178984603669":
				username = userid
				cursor.execute('SELECT * FROM loved')
				loved = cursor.fetchall()
				print(loved)
				loved = str(loved)
				pattern = r'([0-9]+\.%s[0-9]*)'
				loved = re.findall(pattern,loved)
				message1 = message.content
				tolove = re.findall(pattern,message1)
				tolove = tolove[0]
				if userid == "aaa":
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
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			elapsed_time = time.time() - start
			elapsed_time = str(elapsed_time)
			embed = discord.Embed(title="Monage Discord Edition - Credit")
			embed.set_footer(text=" Created message at | " + currenttime + "")
			embed.add_field(name="raspi0124", value=" - 開発・制作")
			embed.add_field(name="脇山P(wakip)", value=" - 大量の資金的な援助及びアドバイス")
			embed.add_field(name="はるまど", value=" - Gitlabの提供")
			embed.add_field(name="lae", value=" - アドバイス、英語文法監修")
			embed.add_field(name="Limit", value=" - helpコマンドの見やすさの向上、リアクションtipのアイデア")
			embed.add_field(name="Ming", value=" - おみくじイラストの作成")
			embed.add_field(name="Bizura", value=" - アイコンの作成")
			embed.add_field(name="kakarichyo", value=" - クローズドアルファにおけるテスト")
			embed.add_field(name="和梨(ポテト)", value=" - クローズドアルファにおけるテスト")
			embed.add_field(name="MGQ", value=" - アドバイス、クローズドアルファにおけるテスト")
			embed.add_field(name="だれかさん", value=" - 新バージョンのテスト・アドバイス")
			embed.add_field(name="Geri", value=" - 新バージョンのテスト・アドバイス")
			embed.add_field(name="その他、Discordサーバー「MGQclub」、「Monacoin」、そして「Monageと遊ぶ鯖」のみなさん", value=" - テスト全般")
			embed.add_field(name="W.S Wsans", value=" - Discord.pyについてのアドバイス")
			embed.add_field(name="ぱい", value=" - Discord.pyについてのアドバイス")
			embed.add_field(name="両親", value=" - 匿名にしておきます")
			await client.send_message(message.channel, embed=embed)



		#MONAPARTY関連スタート

		if message.content.startswith('/mp balance'):
			print("1")
			addresses = mlibs.deposit(userid)
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
			response = requests.post('https://monapa.electrum-mona.org/_api', headers=headers, data=data, auth=('rpc', 'hello'))
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
				num = str(num)
				if num == "0":
					mge = "<@" + userid + ">"
				mge = "" + mge + "\n" + m + ""
			responseresult = str(responseresult)
			await client.send_message(message.channel, mge)

		if message.content.startswith("/mp deposit"):
			# 送り主がBotだった場合反応したくないので
			if client.user != message.author.name:
				# メッセージを書きます
				m = "<@" + userid + "> アドレスを確認中..."
				# メッセージが送られてきたチャンネルへメッセージを送ります
				await client.send_message(message.channel, m)
				address3 = mlibs.deposit(userid)
				m = "<@" + userid + ">, This is your monaparty deposit addresses: " + address3 + "\n(message created on " + currenttime + ")"
				await client.send_message(message.channel, m)

		if message.content.startswith("/mp tip"):
			print("start")
			#beforebal = mlibs.libgetbalance(userid)
			message2 = message.content.replace('/mp tip', '')
			print (message2)
			pattern = r'\w+'
			print(re.findall(pattern,message2))
			tipinfo = re.findall(pattern,message2)
			print(tipinfo[0])
			print(tipinfo[1])
			tipto = tipinfo[0]
			tipamount = tipinfo[1]
			deftipamount = tipinfo[1]
			tiptoken = tipinfo[2]
			#まず最初に数字を取り出す。次にWordを取り出し、とりだしたWordから数字を取り除く。
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
			#APIにアクセスし該当TXIDをもらってくる
			fee = "2000"

			headers = {
				'Content-Type': 'application/json; charset=UTF-8',
				'Accept': 'application/json, text/javascript',
			}

			data = '{"jsonrpc":"2.0", "id":0, "method":"get_asset_info", "params":{"assets":[' + tiptoken + ']} }'

			asset_info = requests.post('http://153.126.176.183:4000/api/ ', headers=headers, data=data, auth=('rpc', 'rpc'))
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

			#手数料で文句言われないようにfee文を予め転送。アカウントシステムだと即座に入れ替わるけどConfの間を縫えば行ける気がする。
			mlibs.withdraw("fee", address, "0.000000005")

			data = '{\n \
  			"method": "create_send",\n \
  			"params": {"source": ' + addresses + ', "destination": ' + tiptoaddress + ', "asset": ' + tiptoken + ', "quantity": ' + tipamount + ', "fee": ' + fee + ', "allow_unconfirmed_inputs": true, "use_enhanced_send": false },\n \
  			"jsonrpc": "2.0",\n \
  			"id": 1\n \
			}'
			print(data)
			repfrom = '"' + tipamount + '"'
			data = data.replace(repfrom, tipamount)



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
			deftipamount = str(deftipamount)
			m = "Successfully sent " + deftipamount + " " + tiptoken + " from <@" + userid + "> to <@" + tipto +"> !\n TXID: " + txid + ""
			await client.send_message(message.channel, m)

	elif message.content.startswith("/"):
		if userid not in ragreedtos:
			for tocheck in commands:
				print("debug:commands")
				print(commands)
				if tocheck in message.content:
					m = "Please agree tos. Type /help for more information.\n 利用規約に同意してください。→　https://github.com/raspi0124/monage-term/blob/master/terms-ja.txt\n Please read tos and try again. Tos can be found at → https://github.com/raspi0124/monage-term/blob/master/terms-en.txt"
					await client.send_message(message.channel, m)
#MONAPARTY関連終わり



	if message.content.startswith("/"):
		if message.content == "/cagreedtos":
			#共用コマンド
			start = time.time()
				# データベース接続とカーソル生成
			# エラー処理（例外処理）
			fee = "0.01"
			m = "<@" + userid + "> おおー、MonageのMonaparty関連の不具合とかを無償で直すことに協力してくださるんですね！ありがたいです！ご協力ありがとうございます！\n <@326091178984603669>! <@" + userid + "> さんがMonapartyの不具合修正に何と無償で協力してくださるそうですよ！ありがいですねー。\nThanks for help us fixing Monaparty on Monage! You are very kind!Now, review the source code and fix it please!"
			await client.send_message(message.channel, m)
			await client.delete_message(message)

		if message.content == "/ragreedtos":
			# データベース接続とカーソル生成
			# エラー処理（例外処理）
			cursor.execute("INSERT INTO ragreedtos (id) VALUES (%s)", (userid,))
			connection.commit()
			m = "<@" + userid + "> 利用規約への同意を確認しました。"
			await client.send_message(message.channel, m)
			if maclib.createmonageid(userid):
				monageid = maclib.getmonageid(userid)
				m = "<@" + userid + "> さんのMonage IDを生成しました! あなたのMonage IDは" + monageid + "です!\n/nregisterコマンドでアドレスを登録しましょう!"
			else:
				m = "MonageIDの生成過程でREDOエラーが起きました。。管理者にメンションします。<@raspi0124>"
			await client.send_message(message.channel, m)
			await client.delete_message(message)
		if message.content == "/agreetos":
			m = "利用規約はきちんと読みましたか？もう一度確認してみましょう。→　https://github.com/raspi0124/monage-term/blob/master/terms-ja.txt\n Please read tos and try again. Tos can be found at → https://github.com/raspi0124/monage-term/blob/master/terms-en.txt"
			await client.send_message(message.channel, m)
		if message.content == "/help":
			start = time.time()
			currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			embed = discord.Embed(title="Monage Discord Edition - Help")
			embed.set_footer(text=" Created message at | " + currenttime + "")
			embed.add_field(name="/help", value=" ヘルプを表示します")
			embed.add_field(name="/nregister ``<あなたのアドレス(Your registering address)>``", value="あなたのアドレスを手動で登録するコマンドです。")
			embed.add_field(name="/updatemyaddress ``<新しいアドレス(Your new address to update)", value="あなたの登録されているアドレスを変更します。")
			embed.add_field(name="/mymonageid", value="あなたのMonage IDを表示します。")
			embed.add_field(name="/deposit", value="あなたの所有しているアドレスを一覧表示します <List all address you have generated>")
			embed.add_field(name="/withdraw ``<amount to withdraw (出金量)> <address to send(アドレス)>``", value="指定されたmonaを指定されたアドレスに送ります <Withdraw specified amount of Mona available to specified address>")
			embed.add_field(name="/tip ``<User to send Mona(送り先ユーザー)> <amount to tip(tip量)> <Comment (optional)>``", value="指定されたmonaを指定されたユーザーに送ります <Tip specified amount of mona to specified user>")
			embed.add_field(name="/checkaddress ``<Target username(対象のユーザー名)``", value="特定のユーザーのアドレスを出力します。")
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

	connection.commit()
	connection.close()
client.run(discord_token)
# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21
