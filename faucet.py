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
from datetime import date
from datetime import datetime
import mlibs
from discord.ext import commands
from ratelimiter import RateLimiter
from discord.ext.commands.cooldowns import BucketType
import sys
from pytz import timezone
import configparser

config = configparser.ConfigParser()
config.read('/root/dismona.conf')

section1 = 'development'
discord_token = config.get(section1, 'discord_token')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')

timestamp = str(time.time())
print("Monage Discord Edition  Copyright (C) 2018  raspi0124\n \
	This program comes with ABSOLUTELY NO WARRANTY; for details, please read https://github.com/raspi0124/dismona/blob/master/LICENSE.\n \
	This is free software, and you are welcome to redistribute it\n \
	under certain conditions; read https://github.com/raspi0124/dismona/blob/master/LICENSE and if you have any question, email to raspi0124[@]gmail.com.")

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
connection = MySQLdb.connect(
	host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
cursor = connection.cursor()
@client.event
@commands.cooldown(1, 5, BucketType.user)
async def on_message(message):
	connection = MySQLdb.connect(
		host=db_host, user=db_user, passwd=db_password, db=db_name, charset='utf8')
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	cursor.execute('SELECT * FROM agreetos')
	agreetos = cursor.fetchall()
	agreetos = mlibs.fixselect(agreetos)
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
	JST = timezone('Asia/Tokyo')

	if message.content.startswith("/") and message.content != "/agreetos" and message.content != "/ragreedtos" and message.content != "/cagreedtos" and message.content != "/help" and userid in ragreedtos:
		# 全件取得は cursor.fetchall()
		# 「/register」で始まるか調べる
		if message.content == "/kill faucet":
			if userid == "326091178984603669":
				m = "OK, Killing faucet process.."
				await client.send_message(message.channel, m)
				sys.exit()


		if message.content == "/shootizaya":
			izaya_sleep = 0.5
			try:
				print("shootizaya executed")
				cursor.execute("SELECT * from shooted")
				isadded = cursor.fetchall()
				INTTIMES = "3"
				if userid not in isadded:
					print("1")
					cursor.execute("INSERT INTO shooted (id, times) VALUES (%s, %s)", (userid, INTTIMES))
					connection.commit()
				print("2")
				cursor.execute("SELECT times FROM shooted WHERE id = %s", (userid,))
				remainshootedtimes = cursor.fetchall()
				print(remainshootedtimes)
				remainshootedtimes = str(remainshootedtimes)
				pattern = r'([+-]?[0-9]+\.?[0-9]*)'
				tmp = re.findall(pattern,remainshootedtimes)
				remainshootedtimes = tmp[0]
				print("3")
				cursor.execute('SELECT banedid FROM baned')
				baned = cursor.fetchall()
				baned = str(baned)
				baned = baned.replace('(', '')
				baned = baned.replace(')', '')
				baned = baned.replace("b'", '')
				baned = baned.replace("'", '')
				baned = baned.replace(",,", ',')
				baned = baned.replace("[", '')
				baned = baned.replace("]", '')
				baned = baned.split(',')
				baned = str(baned)
				if message.author.id not in baned:
					#Izaya鯖かそれ以外化で表示等を分ける。なお最初はIzaya鯖でないときの処理、次がIzaya鯖の時の処理
					if message.server.id != "392277276470804480":
						def result():
							kuji = ["0", "1", "2", "3", "4", "5"]
							result = random.choice(kuji)
							return result
						separator = '-'
						result = result()
						with rate_limiter:
							print("4")
							cursor.execute("SELECT hp FROM hp ORDER BY timestamp DESC")
						currenthp = cursor.fetchall()
						print(currenthp)
						currenthp = str(currenthp)
						pattern=r'([+-]?[0-9]+\.?[0-9]*)'
						print(re.findall(pattern,currenthp))
						currenthp = re.findall(pattern,currenthp)
						print(currenthp[0])
						currenthp = int(currenthp[0])
						with rate_limiter:
							if remainshootedtimes > "0":
								if result == "0" or result == "1" or result == "2":
									nowhp = currenthp - int("5")
									nowhp = str(nowhp)
									print(nowhp)
									m = "(´・ω);y==ｰｰｰｰｰ  ・ ・   <:izaya:441956642125512734>    ・∵. ﾀｰﾝ\nIzayaに 5 ダメージを与えた！\nIzayaの現在のHPは " + nowhp + " だ。"
									toedit = await client.send_message(message.channel, m)
									print("5")
									cursor.execute("INSERT INTO hp (timestamp, hp) VALUES (%s, %s)", (timestamp, nowhp))
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "(´・ω);y==ｰｰｰｰｰ  ・ ・   <:izaya:441956642125512734>    ・∵. ﾀｰﾝ\nIzayaに 5 ダメージを与えた！")
								if result == "3":
									currenthp = str(currenthp)
									m = "(´・ω);y==ｰｰｰｰｰ  ・ ・ ・   ｶﾝ∵.  <:biso:444368914814730251> <:izaya:441956642125512734>＜ﾋﾞﾝﾋﾞﾝｶﾞｰﾄﾞ\n残念。。防がれてしまった。。\nIzayaの現在のHPは " + currenthp + " だ。"
									toedit = await client.send_message(message.channel, m)
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "(´・ω);y==ｰｰｰｰｰ  ・ ・ ・   ｶﾝ∵.  <:biso:444368914814730251> <:izaya:441956642125512734>＜ﾋﾞﾝﾋﾞﾝｶﾞｰﾄﾞ\n残念。。防がれてしまった。。")
								if result == "4":
									nowhp = currenthp - int("10")
									nowhp = str(nowhp)
									print(nowhp)
									m = "（っ'-')╮        ﾌﾞｫﾝ =͟͟͞: :poop:       <:izaya:441956642125512734>    ・∵. ﾊﾟｰﾝ ---==( ε : )0\nIzayaに 10 ダメージを与えた！\nIzayaの現在のHPは " + nowhp + " だ。"
									toedit = await client.send_message(message.channel, m)
									print("6")
									cursor.execute("INSERT INTO hp (timestamp, hp) VALUES (%s, %s)", (timestamp, nowhp))
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "（っ'-')╮        ﾌﾞｫﾝ =͟͟͞: :poop:       <:izaya:441956642125512734>    ・∵. ﾊﾟｰﾝ ---==( ε : )0\nIzayaに 10 ダメージを与えた！")
								if result == "5":
									currenthp = str(currenthp)
									m = "Izaya は、どこかへ逃げてしまった！\n残念。。当てられなかった..\nIzayaの現在のHPは " + currenthp + " だ。"
									toedit = await client.send_message(message.channel, m)
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "Izaya は、どこかへ逃げてしまった！\n残念。。当てられなかった..")
								mlibs.tip("izaya", userid, "0.00000001")
								m = "攻撃報酬 1 watanabe 獲得!！\nこれからも討伐協力よろしくお願いします！"
								await client.send_message(message.channel, m)
								print("7")
								cursor.execute("SELECT hp FROM hp ORDER BY timestamp DESC")
								currenthp = cursor.fetchall()
								print(currenthp)
								currenthp = str(currenthp)
								pattern=r'([+-]?[0-9]+\.?[0-9]*)'
								print(re.findall(pattern,currenthp))
								currenthp = re.findall(pattern,currenthp)
								print(currenthp[0])
								currenthp = int(currenthp[0])
								#define hp
								MINHP = int("0")

								nowremainshootedtimes = int(remainshootedtimes) - int("1")
								print("8")
								cursor.execute("UPDATE shooted SET times = %s WHERE id = %s", (nowremainshootedtimes, userid))



								if currenthp <= MINHP:
									m = "討伐を達成しました\nクエスト報酬を獲得しました！(100watanabe)"
									await client.send_message(message.channel, m)
									mlibs.tip("izaya", userid, "0.00000100")
									m = ":scroll:上位クエスト:scroll:が解放されました！(スポンサー） \n https://discord.gg/RmRevCV"
									await client.send_message(message.channel, m)
									newhp = random.randint(100,150)
									print("9")
									cursor.execute("INSERT INTO hp (timestamp, hp) VALUES (%s, %s)", (timestamp, newhp))
									newhp = str(newhp)
									m = "次のHPは " + newhp + "です!"
									torm = await client.send_message(message.channel, m)
									time.sleep(3)
									await client.delete_message(torm)

								#if remainshootedtimes == "1"の手法だとなぜか動かなかったのでinを使用。
								remainshootedtimes = str(remainshootedtimes)
								if remainshootedtimes == "1":
									m = "あなたはあと0回shootizayaを実行できます！"
									await client.send_message(message.channel, m)
								if remainshootedtimes == "2":
									m = "あなたはあと1回shootizayaを実行できます！"
									await client.send_message(message.channel, m)
								print("--nowremainshootedtimes--")
								print(nowremainshootedtimes)
							elif remainshootedtimes <= "0":
								m = "1日3回しか実行できません。"
								await client.send_message(message.channel, m)
					else:
						def result():
							kuji = ["0", "1", "2", "3", "4", "5"]
							result = random.choice(kuji)
							return result
						separator = '-'
						result = result()
						with rate_limiter:
							print("4")
							cursor.execute("SELECT hp FROM hp ORDER BY timestamp DESC")
						currenthp = cursor.fetchall()
						print(currenthp)
						currenthp = str(currenthp)
						pattern=r'([+-]?[0-9]+\.?[0-9]*)'
						print(re.findall(pattern,currenthp))
						currenthp = re.findall(pattern,currenthp)
						print(currenthp[0])
						currenthp = int(currenthp[0])
						with rate_limiter:
							if remainshootedtimes > "0" :
								if result == "0" or result == "1" or result == "2":
									nowhp = currenthp - int("5")
									nowhp = str(nowhp)
									print(nowhp)
									m = "(´・ω);y==ｰｰｰｰｰ  ・ ・   <:izaya:441956642125512734>    ・∵. ﾀｰﾝ\nIzayaに 5 ダメージを与えた！\nIzayaの現在のHPは " + nowhp + " だ。"
									toedit = await client.send_message(message.channel, m)
									print("5")
									cursor.execute("INSERT INTO hp (timestamp, hp) VALUES (%s, %s)", (timestamp, nowhp))
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "(´・ω);y==ｰｰｰｰｰ  ・ ・   <:izaya:441956642125512734>    ・∵. ﾀｰﾝ\nIzayaに 5 ダメージを与えた！")
								if result == "3":
									currenthp = str(currenthp)
									m = "(´・ω);y==ｰｰｰｰｰ  ・ ・ ・   ｶﾝ∵.  <:biso:444368914814730251> <:izaya:441956642125512734>＜ﾋﾞﾝﾋﾞﾝｶﾞｰﾄﾞ\n残念。。防がれてしまった。。\nIzayaの現在のHPは " + currenthp + " だ。"
									toedit = await client.send_message(message.channel, m)
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "(´・ω);y==ｰｰｰｰｰ  ・ ・ ・   ｶﾝ∵.  <:biso:444368914814730251> <:izaya:441956642125512734>＜ﾋﾞﾝﾋﾞﾝｶﾞｰﾄﾞ\n残念。。防がれてしまった。。")
								if result == "4":
									nowhp = currenthp - int("10")
									nowhp = str(nowhp)
									print(nowhp)
									m = "（っ'-')╮        ﾌﾞｫﾝ =͟͟͞: :poop:       <:izaya:441956642125512734>    ・∵. ﾊﾟｰﾝ ---==( ε : )0\nIzayaに 10 ダメージを与えた！\nIzayaの現在のHPは " + nowhp + " だ。"
									toedit = await client.send_message(message.channel, m)
									print("6")
									cursor.execute("INSERT INTO hp (timestamp, hp) VALUES (%s, %s)", (timestamp, nowhp))
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "（っ'-')╮        ﾌﾞｫﾝ =͟͟͞: :poop:       <:izaya:441956642125512734>    ・∵. ﾊﾟｰﾝ ---==( ε : )0\nIzayaに 10 ダメージを与えた！")
								if result == "5":
									currenthp = str(currenthp)
									m = "Izaya は、どこかへ逃げてしまった！\n残念。。当てられなかった..\nIzayaの現在のHPは " + currenthp + " だ。"
									toedit = await client.send_message(message.channel, m)
									time.sleep(izaya_sleep)
									await client.edit_message(toedit, "Izaya は、どこかへ逃げてしまった！\n残念。。当てられなかった..")
								mlibs.tip("izaya", userid, "0.00000002")
								m = "攻撃報酬 2 watanabe 獲得!！\nこれからも討伐協力よろしくお願いします！"
								await client.send_message(message.channel, m)
								print("7")
								cursor.execute("SELECT hp FROM hp ORDER BY timestamp DESC")
								currenthp = cursor.fetchall()
								print(currenthp)
								currenthp = str(currenthp)
								pattern=r'([+-]?[0-9]+\.?[0-9]*)'
								print(re.findall(pattern,currenthp))
								currenthp = re.findall(pattern,currenthp)
								print(currenthp[0])
								currenthp = int(currenthp[0])
								#define hp
								MINHP = int("0")

								nowremainshootedtimes = int(remainshootedtimes) - int("1")
								print("8")
								cursor.execute("UPDATE shooted SET times = %s WHERE id = %s", (nowremainshootedtimes, userid))



								if currenthp <= MINHP:
									m = "討伐を達成しました\nクエスト報酬を獲得しました！(200watanabe)"
									await client.send_message(message.channel, m)
									mlibs.tip("izaya", userid, "0.00000200")
									m = ":scroll:上位クエスト:scroll:が解放されました！(スポンサー） \n https://discord.gg/RmRevCV"
									await client.send_message(message.channel, m)
									newhp = random.randint(100,150)
									print("9")
									cursor.execute("INSERT INTO hp (timestamp, hp) VALUES (%s, %s)", (timestamp, newhp))
									newhp = str(newhp)
									m = "次のHPは " + newhp + "です!"
									torm = await client.send_message(message.channel, m)
									time.sleep(10)
									await client.delete_message(torm)

								#if remainshootedtimes == "1"の手法だとなぜか動かなかったのでinを使用。
								if remainshootedtimes == "1":
									m = "あなたはあと0回shootizayaを実行できます！"
									await client.send_message(message.channel, m)
								if remainshootedtimes == "2":
									m = "あなたはあと1回shootizayaを実行できます！"
									await client.send_message(message.channel, m)
								print("--nowremainshootedtimes--")
								print(nowremainshootedtimes)
							elif remainshootedtimes <= "0":
								m = "1日3回しか実行できません。"
								await client.send_message(message.channel, m)
				else:
					cursor.execute("SELECT banfromid FROM baned WHERE bandid = %s", (userid,) )
					banfromid = cursor.fetchall()
					banfromid = banfromid[0]
					cursor.execute("SELECT reason FROM baned WHERE bandid = %s", (userid,) )
					banreason = cursor.fetchall()
					banreason = banreason[0]
					m = "<@" + message.author.id  + "> あなたは <@" + banfromid + "> によって以下の理由でBANされています。 " + banreason + " "
					await client.send_message(message.channel, m)
			except _mysql_exceptions.OperationalError:
				m = "Izaya は、どこかへ逃げてしまった！\n残念。。当てられなかった.. (Code: 500)"
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
			print("1")
			cursor.execute('SELECT banedid FROM baned')
			baned = cursor.fetchall()
			print("2")
			cursor.execute('SELECT * FROM tiped')
			tiped = cursor.fetchall()
			tiped = list(tiped)
			tiped = str(tiped)
			tiped = tiped.replace('(', '')
			tiped = tiped.replace(')', '')
			tiped = tiped.replace("b'", '')
			tiped = tiped.replace("'", '')
			tiped = tiped.replace(",,", ',')
			tiped = tiped.replace("[", '')
			tiped = tiped.replace("]", '')
			tiped = tiped.split(',')
			tiped = str(tiped)
			pattern = r'([0-9]+\.%s[0-9]*)'
			tiped = re.findall(pattern,tiped)
			print("3")
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
			pattern = r'([0-9]+\.%s[0-9]*)'
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
					m = "<@" + userid + "> 貴方の今日の運勢は" + resultp + "です!"
					await client.send_message(message.channel, m)
					cursor.execute("INSERT INTO gived (id) VALUES (%s)", (username,))
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
					origresult=result
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
					if result == kyou:
						m = "あなたの運勢…凶みたいだから、今日はそばにいてあげるんだからねっ！今日だけだからねっ"
					else:
						m = "<@" + userid + "> ダーリン、あなたの今日の運勢は" + resultp + "らしいですわよ。! 今日も気をつけてね、ダーリン。 . exectime: " + elapsed_time + " sec"
					await client.send_message(message.channel, m)
					cursor.execute("INSERT INTO gived (id) VALUES (%s)", (username,))
					if origresult > 0:
						m = "/tip <@" + username + "> 0.000" + result + ""
						await client.send_message(message.channel, m)
					connection.commit()
			else:
				m = "<@" + userid +"> すでに今日におみくじをされているようです。。明日戻ってきてね！"
				await client.send_message(message.channel, m)

		if message.content == "/omikuzi" or message.content == "/omikuji":
			start = time.time()
			username = message.author.id
			print("omikuzi executed 1")

			cursor.execute('SELECT * FROM gived')
			gived = cursor.fetchall()
			gived = str(gived)
			gived = gived.replace('(', '')
			gived = gived.replace(')', '')
			gived = gived.replace("b'", '')
			gived = gived.replace("'", '')
			gived = gived.replace(",,", ',')
			gived = gived.replace("[", '')
			gived = gived.replace("]", '')
			gived = gived.split(',')
			gived = str(gived)

			cursor.execute('SELECT banedid FROM baned')
			baned = cursor.fetchall()
			baned = str(baned)
			baned = baned.replace('(', '')
			baned = baned.replace(')', '')
			baned = baned.replace("b'", '')
			baned = baned.replace("'", '')
			baned = baned.replace(",,", ',')
			baned = baned.replace("[", '')
			baned = baned.replace("]", '')
			baned = baned.split(',')
			baned = str(baned)

			cursor.execute('SELECT * FROM tiped')
			tiped = cursor.fetchall()
			tiped = str(tiped)
			tiped = tiped.replace('(', '')
			tiped = tiped.replace(')', '')
			tiped = tiped.replace("b'", '')
			tiped = tiped.replace("'", '')
			tiped = tiped.replace(",,", ',')
			tiped = tiped.replace("[", '')
			tiped = tiped.replace("]", '')
			tiped = tiped.split(',')
			tiped = str(tiped)
			print(tiped)

			gived = str(gived)
			tiped = str(tiped)
			print("--gived--")
			print(gived)
			minlimit = "0.005"
			balance = mlibs.libgetbalance(userid)
			await client.add_reaction(message, '👌')
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
			balance = float(balance)
			minlimit = float(minlimit)
			print("3")
			cursor.execute('SELECT * FROM ragreedtos')
			ragreedtos = cursor.fetchall()
			ragreedtos = mlibs.fixselect(ragreedtos)
			if userid not in ragreedtos:
				if username not in gived:
					if balance >= minlimit:
						if username not in baned:
							if username in tiped:
								if username not in loved:
									def omikuji():
										kuji = ["0", "1", "2", "3", "1", "2", "7", "1", "2", "3", "1", "2", "3", "2", "3", "2", "0", "0"]
										result = random.choice(kuji)
										return result
									kuji = ["凶", "小吉", "中吉", "大吉", "凶", "小吉", "中吉", "超大吉"]
									resultnumber = omikuji()
									resultnumber = int(resultnumber)
									print("resultnumber")
									print(resultnumber)
									addamount = "1"
									resultnumber = int(resultnumber)
									origresnum = resultnumber
									resultword = kuji[resultnumber]
									resultgive = float(resultnumber) + float(addamount)
									resultgive = int(resultgive)
									print("resultgive")
									print(resultgive)
									resultgive = str(resultgive)
									resultgive = int(resultgive)
									resultgive = str(resultgive)
									resultnumber = str(resultnumber)
									#以下のif列のresultの書き換えがめんどくさかったからここで処理
									result = resultnumber
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
									username = int(username)
									username = str(username)
									print("INSERT INTO gived (id) VALUES (" + username + ")")
									cursor.execute("INSERT INTO gived (id) VALUES (" + username + ")")
									if origresnum > 0:
										m = "/tip <@" + username + "> 0.0000" + resultgive + " おみくじtipです！貴方の今日の運勢は" + resultword + "です!次挑戦できるのは日本時間で明日です！"
										await client.send_message(message.channel, m)
									connection.commit()
								else:
									def omikuji():
										kuji = ["0", "1", "2", "3", "2", "4"]
										result = random.choice(kuji)
										return result
									kuji = ["凶", "小吉", "中吉", "大吉", "超大吉"]
									resultnumber = omikuji()
									print("resultnumber")
									print(resultnumber)
									resultnumber = int(resultnumber)
									origresnum = resultnumber
									print("resultnumber")
									print(resultnumber)
									resultword = kuji[resultnumber]
									resultword = str(resultword)
									resultgive = float(resultnumber) + float("3")
									resultgive = int(resultgive)
									resultgive = str(resultgive)
									resultnumber = str(resultnumber)
									#以下のif列のresultの書き換えがめんどくさかったからここで処理
									result = resultnumber
									if resultnumber == "0":
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
									result = str(result)
									origresnum = str(origresnum)
									if result == "0":
										m = "あなたの運勢…凶みたいだから、今日はそばにいてあげるんだからねっ！今日だけだからねっ"
									else:
										m = "<@" + userid +">ダーリン、あなたの今日の運勢は" + resultword + "らしいですわよ。!\n0.000" + resultgive + "Mona送ってあげるわ。今日も気をつけてね、ダーリン。"
									await client.send_message(message.channel, m)
									cursor.execute("INSERT INTO gived (id) VALUES (%s)", (username,))
									if origresnum != "0":
										m = "/tip <@" + username + "> 0.000" + resultgive + ""
										await client.send_message(message.channel, m)
									connection.commit()
							else:
								m = "<@" + userid +">スパム対策のために今日Tipした、またはされていない方ははおみくじを実行することができません。。だれかにtipするかtipされてからもう一回実行おねがいします\nTo prevent spamming, user who never tiped today or user  who never get tiped today are not allowed to execute omikuji. please tip someone using /tip command."
								await client.send_message(message.channel, m)
						else:
							cursor.execute('SELECT banfromid FROM baned WHERE banedid = ' + username + '')
							banfromid = cursor.fetchall()
							banfromid = str(banfromid)
							m = "<@" + userid + ">You are not allowed to /omikuzi! \n Detail:You are baned by <@" + banfromid + ">"
							await client.send_message(message.channel, m)
					else:
						m = "残高がMinlimit(0.005mona)に達していないためおみくじを実行することはできません。"
						await client.send_message(message.channel, m)
				else:
					m = "もう、<@" + message.author.id + "> 、何やってるの！！\n おみくじは1日一回ってあんなに言ったでしょ！ 明日まで禁止よ！\nそこに座ってなさい！"
					await client.send_message(message.channel, m)
			else:
				if username not in gived:
					if balance >= minlimit:
						if username not in baned:
							if username in tiped:
								if username not in loved:
									def omikuji():
										kuji = ["0", "1", "2", "3", "1", "2", "7", "1", "2", "3", "1", "2", "3", "2", "3", "2", "0", "0"]
										result = random.choice(kuji)
										return result
									kuji = ["凶", "小吉", "中吉", "大吉", "凶", "小吉", "中吉", "超大吉"]
									resultnumber = omikuji()
									resultnumber = int(resultnumber)
									print("resultnumber")
									print(resultnumber)
									addamount = "1"
									resultnumber = int(resultnumber)
									origresnum = resultnumber
									resultword = kuji[resultnumber]
									resultgive = float(resultnumber) + float(addamount)
									resultgive = int(resultgive)
									print("resultgive")
									print(resultgive)
									resultgive = str(resultgive)
									resultgive = int(resultgive)
									resultgive = str(resultgive)
									resultnumber = str(resultnumber)
									#以下のif列のresultの書き換えがめんどくさかったからここで処理
									result = resultnumber
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
									username = int(username)
									username = str(username)
									print("INSERT INTO gived (id) VALUES (" + username + ")")
									cursor.execute("INSERT INTO gived (id) VALUES (" + username + ")")
									if origresnum > 0:
										m = "/tip <@" + username + "> 0.000000" + resultgive + " おみくじtipです！貴方の今日の運勢は" + resultword + "です!次挑戦できるのは日本時間で明日です！"
										await client.send_message(message.channel, m)
									connection.commit()
								else:
									def omikuji():
										kuji = ["0", "1", "2", "3", "2", "4"]
										result = random.choice(kuji)
										return result
									kuji = ["凶", "小吉", "中吉", "大吉", "超大吉"]
									resultnumber = omikuji()
									print("resultnumber")
									print(resultnumber)
									resultnumber = int(resultnumber)
									origresnum = resultnumber
									print("resultnumber")
									print(resultnumber)
									resultword = kuji[resultnumber]
									resultword = str(resultword)
									resultgive = float(resultnumber) + float("3")
									resultgive = int(resultgive)
									resultgive = str(resultgive)
									resultnumber = str(resultnumber)
									#以下のif列のresultの書き換えがめんどくさかったからここで処理
									result = resultnumber
									if resultnumber == "0":
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
									result = str(result)
									origresnum = str(origresnum)
									if result == "0":
										m = "あなたの運勢…凶みたいだから、今日はそばにいてあげるんだからねっ！今日だけだからねっ"
									else:
										m = "<@" + userid +">ダーリン、あなたの今日の運勢は" + resultword + "らしいですわよ。!\n0.000" + resultgive + "Mona送ってあげるわ。今日も気をつけてね、ダーリン。"
									await client.send_message(message.channel, m)
									cursor.execute("INSERT INTO gived (id) VALUES (%s)", (username,))
									if origresnum != "0":
										m = "/tip <@" + username + "> 0.00000" + resultgive + ""
										await client.send_message(message.channel, m)
									connection.commit()
							else:
								m = "<@" + userid +">スパム対策のために今日Tipした、またはされていない方ははおみくじを実行することができません。。だれかにtipするかtipされてからもう一回実行おねがいします\nTo prevent spamming, user who never tiped today or user  who never get tiped today are not allowed to execute omikuji. please tip someone using /tip command."
								await client.send_message(message.channel, m)
						else:
							cursor.execute('SELECT banfromid FROM baned WHERE banedid = ' + username + '')
							banfromid = cursor.fetchall()
							banfromid = str(banfromid)
							m = "<@" + userid + ">You are not allowed to /omikuzi! \n Detail:You are baned by <@" + banfromid + ">"
							await client.send_message(message.channel, m)
					else:
						m = "残高がMinlimit(0.005mona)に達していないためおみくじを実行することはできません。"
						await client.send_message(message.channel, m)
				else:
					m = "もう、<@" + message.author.id + "> 、何やってるの！！\n おみくじは1日一回ってあんなに言ったでしょ！ 明日まで禁止よ！\nそこに座ってなさい！"
					await client.send_message(message.channel, m)
		if message.content == "/お年玉ちょうだい":
			#めんどくさくなって日時指定なくしたので三が日終わったら消してね
			cursor.execute('SELECT * FROM given_otoshidama')
			given_otoshidama = cursor.fetchall()
			print(given_otoshidama)
			print(userid)
			if userid not in given_otoshidama:
				balance = mlibs.libgetbalance(userid)
				#残高の20分の1
				giving = float(balance) * float("0.05")
				minimum = float("0.00010")
				maximum = float("0.2")
				cursor.execute("INSERT INTO given_otoshidama (id) VALUES (%s)", (userid,))
				connection.commit()
				if giving < minimum:
					m = "/tip <@" + userid + "> 0.0001 あけおめです！あ、金欠なraspi0124君にもお年玉くれるとうれしいな♪"
					await client.send_message(message.channel, m)
				else:
					if giving > maximum:
						m = "/tip <@" + userid + "> 0.2 2018年はよく使ってくれてありがとう！今年もよろしくお願いします！そしてあけましておめでとうございます!~~（金欠なraspi0124君にもお年玉くれるといいな- ~~"
						await client.send_message(message.channel, m)
					else:
						giving = str(giving)
						m = "/tip <@" + userid + "> " + giving + " 去年はありがとうございます!今年もよろしくお願いします!そしてあけおめ!~~あ、あと金欠なraspi0124君にもお年玉くれるとうれしいです!~~"
						await client.send_message(message.channel, m)

	connection.commit()
	connection.close()
client.run(discord_token)
