	# -*- coding:utf-8 -*-
import json
import falcon
import sqlite3
from datetime import datetime
class WalletAPI(object):
	file = open('../zenipota-log.txt', 'w')  #書き込みモードでオープン
	currenttime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	dbpath = '../zenipota.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	print("1")
	# postされた時の動作
	def on_get(self, req, resp, project_id):
		print(req)
		print(self)
		print(res)
		print (req.params)
		print(req.stream.read())
		dir(req)
	def on_post(self, req, res):
		print("2")
		#print(req.stream.read())
		# postパラメーターを取得
		body = req.stream.read()
		print(body)
		body = body.decode()
		print(body)
		body = str(body)
		print(body)
		data = json.load()
		data = str(data)
		print("3")
		# パラメーターの取得
		username = data['username']
		action = data['action']
		cmd = "bitzeny-cli getbalance "  + username + ""
		balance  =  subprocess.check_output( cmd.split(" ") )
		print(balance)
		print("4")
		if action == "register":
			string = "" + currenttime + " Register requested with username:" + username + ""
			password = data['password']
			cursor.execute('SELECT username FROM payment')
			users = cursor.fetchall()
			print(users)
			users = str(users)
			pattern = r'(*)'
			users = re.findall(pattern,users)
			if username not in users:
				string = "" + currenttime + " Registered username:" + username + ""
				cursor.execute("INSERT INTO userinfo (username, password) VALUES (?,?)", (username, password))
				#cmd = "bitzeny-cli getnewaddress "  + username + ""
				#ruta  =  subprocess.check_output( cmd.split(" ") )
				#print(ruta)
				m = "success_register_user_" + username + ""
				print(m)
				msg = {
					"message": "" + m + ""
				}

			else:
				string = "" + currenttime + " Already registered:" + username + ""
				m = "already_exist_register_user_" + username + ""
				msg = {
					"message": "" + m + ""
				}

		if action == "getbalance":
			string = "" + currenttime + " Balance requested username:" + username + ""
			cmd = "bitzeny-cli getbalance "  + username + ""
			ruta  =  subprocess.check_output( cmd.split(" ") )
			print(ruta)
			msg = {
				"message": "" + ruta + ""
			}
		if action == "getaddress":
			string = "" + currenttime + " Address requested with username:" + username + ""
			cmd = "bitzeny-cli getaddressesbyaccount " + username + ""
			ruta  =  subprocess.check_output( cmd.split(" ") )
			print(ruta)
			msg = {
				"message": "" + ruta + ""
			}
		if action == "move":
			moveto = data['moveto']
			password = data["password"]
			amounttomove = data["amount"]
			string = "" + currenttime + " Move requested with username:" + username + ""
			if balance >= amounttomove:
				string = "" + currenttime + " Moved" + amounttomove + "to " + moveto + " username:" + username + ""
				cmd = "bitzeny-cli move " + username + " " + moveto + " " + amount + ""
				ruta  =  subprocess.check_output( cmd.split(" ") )
				print(ruta)
				if ruta == "true":
					msg = {
						"message": "true"
					}
				else:
					msg = {
					"message": "false"
					}
		if action == "withdraw":
			withdrawto = data["withdrawto"]
			amounttowithdraw = data["amount"]
			if balance >= amounttowithdraw:
				cmd = "bitzeny-cli sendfrom " + username + " " + withdrawto + " " + amounttowithdraw + ""
				ruta  =  subprocess.check_output( cmd.split(" ") )
				print(ruta)
				msg = {
					"message": "true"
				}
			else:
				msg = {
					"message": "false"
				}
		if action == "ping":
			msg = {
			"message": "pong"
			}


		else:
			msg = {
			"message": "No method found. Hackers? How did you find here?"
			}
			print("5")


		msg = str(msg)
		res.body = json.dumps(msg)
		print("6")
		file.write(string)
app = falcon.API()
app.add_route("/", WalletAPI())
if __name__ == "__main__":
	from wsgiref import simple_server
	httpd = simple_server.make_server("0.0.0.0", 8000, app)
	httpd.serve_forever()
