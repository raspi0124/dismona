import subprocess
import re
import time
import math
import random
import json
import requests
import decimal
import falcon
import mlibs
from decimal import (Decimal, ROUND_DOWN)
class API(object):
	print("1")
	def on_post(self, req, res):
		# postパラメーターを取得
		body = req.stream.read()
		print(body)
		body = body.decode()
		body = str(body)
		print(body)
		data = json.loads(body)
		print(body)
		print("3")
		currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		# パラメーターの取得
		action = data['action']
		print("4")
		prohibate = [" ", "(", ")", "&", ";", ":", "=", "!", "*", "{", "}", "[", "]", "/", "'", '"', "|", "~", "^",]

		if action == "getaddress":
			username = data['username']
			if prohibate not in username:
				username = data['username']
				string = "Address requested with username:" + username + ""
				ruta = mlibs.deposit(username)
				ruta = str(ruta)
				msg = { "message": "" + ruta + "" }
		if action == "getbalance":
			username = data['username']
			username = data['username']
			string = "Balance requested with username:" + username + ""
			ruta = mlibs.libgetbalance(username)
			ruta = str(ruta)
			msg = { "message": "" + ruta + "" }
		if action == "ping":
			msg = {
			"message": "pong"
			}
		msg = str(msg)
		msg = msg.replace('\n','')
		msg = str(msg)
		res.body = json.dumps(msg)
		print("6")
app = falcon.API()
app.add_route("/", API())
if __name__ == "__main__":
	from wsgiref import simple_server
	httpd = simple_server.make_server("0.0.0.0", 8354, app)
	httpd.serve_forever()
